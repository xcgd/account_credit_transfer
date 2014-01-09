from openerp.osv import fields, osv
from openerp.tools.translate import _

from base64 import b64decode, encodestring

from tempfile import NamedTemporaryFile

from genshi.template import TemplateLoader,\
    TemplateNotFound, TemplateSyntaxError


class SepaBase(object):
    def compute(self, file_bin, data):
        with NamedTemporaryFile(
            suffix=".xml", prefix="genshi-template-"
        ) as temp_file:
            print b64decode(file_bin)
            temp_file.write(b64decode(file_bin))
            temp_file.flush()
            template_loader = TemplateLoader()
            try:
                tpl = template_loader.load(temp_file.name)
            except TemplateNotFound as e:
                raise osv.except_osv(_('Template Not Found'), e)
            except TemplateSyntaxError as e:
                raise osv.except_osv(_('Template Syntax Error'), e)
            content = str(tpl.generate(data=data))
        print content
        fname = "PAYMENT%s%s.xml" % (
            data['batch'].name.replace(" ", ""),
            data['date']
        )
        att_values = {
            'datas': encodestring(content),
            'datas_fname': fname,
            'name': fname,
            'res_id': data['batch'].id,
            'res_model': 'account.voucher.sepa_batch',
        }
        return att_values


class SepaSG(SepaBase):
    def compute(self, tpl, data):
        res = super(SepaSG, self).compute(tpl, data)
        return res


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
        if parser.parser == 'sepa_sg':
            return SepaSG()
