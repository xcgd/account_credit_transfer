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
            temp_file.write(b64decode(file_bin))
            temp_file.flush()
            template_loader = TemplateLoader()
            try:
                tpl = template_loader.load(temp_file.name)
            except TemplateNotFound as e:
                raise osv.except_osv(_('Template Not Found'), e)
            except TemplateSyntaxError as e:
                raise osv.except_osv(_('Template Syntax Error'), e)
            content = tpl.generate(data=data).render('xml')
        fname = "PAYMENT%s%s.xml" % (
            data['batch'].name.replace(" ", ""),
            data['date']
        )
        att_values = {
            'datas': encodestring(content.encode('utf-8')),
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
        ('sepa_sg', 'Sepa - pain'),
    ]

    def _get_template_visual(self, cr, uid, ids, name, args, context=None):
        res = {}
        brs = self.browse(cr, uid, ids, context=context)
        for br in brs:
            res[br.id] = b64decode(br.template) if br.template else None
        return res

    _columns = {
        "name": fields.char("Name", size=256, required=True),
        "parser": fields.selection(
            _enum_parser,
            required=True,
            string="Parser",
        ),
        "type": fields.selection(
            [("transfer", "Transfer"),
             ("direct_debit", "Direct Debit")],
            required=True,
            string="Type",
            help="The type of operation"
        ),
        "bank": fields.many2one(
            "res.bank",
            string="Bank",
            help="Fill this field if the parser is specific to a"
                 "particular bank",
        ),
        "template": fields.binary(
            'Template',
            required=True,
            filters='*.xml',
        ),
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

    _defaults = {
        "type": "transfer",
    }

    def get_parser(self, cr, uid, parser, context=None):
        if parser.parser == 'sepa_sg':
            return SepaSG()
