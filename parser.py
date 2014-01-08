from openerp.osv import fields, osv
from base64 import b64decode


class SepaBase(object):
    def load_template(self, file_bin):
        template_loader = TemplateLoader(
            [os.path.dirname(os.path.abspath(__file__))])
        try:
            return template_loader.load(TEMPLATE)
        except TemplateNotFound as e:
            raise osv.except_osv(_('Template Not Found'), e)
        except TemplateSyntaxError as e:
            raise osv.except_osv(_('Template Syntax Error'), e)


class SepaSG(SepaBase):
    def compute(self, file_name):
        return super(SepaSG, self).parse(file_name)


class credit_transfer_parser(osv.Model):
    _name = "account_credit_transfer.parser"

    _enum_parser = [
        ('sepa_sg', 'Sepa - Societe Generale'),
    ]

    def name_get(self, cr, uid, ids, context=None):
        brs = self.browse(cr, uid, ids, context=context)
        res = []

        for br in brs:
            res.append(
                (br.id,
                 [x[1] for x in self._enum_parser if x[0] == br.parser][0]),
            )
        return res

    def _get_template_visual(self, cr, uid, ids, name, args, context=None):
        res = {}
        brs = self.browse(cr, uid, ids, context=context)
        for br in brs:
            res[br.id] = b64decode(br.template) if br.template else None
        return res

    _columns = {
        "parser": fields.selection(
            _enum_parser,
            string="Parser",
        ),
        "template": fields.binary(),
        "template_visual": fields.function(
            _get_template_visual,
            type="text",
            method=True,
            string="Template",
            store={
                "account_credit_transfer.parser": (
                    lambda self, cr, uid, ids, c={}: ids,
                    ["template"],
                    10
                ),
            },
        )
    }

    def get_parser(self, cr, uid, parser, context=None):
        if parser.parser == 'test':
            return SepaSG(parser.template)
