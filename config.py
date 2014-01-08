from openerp.osv import fields, osv
from genshi.template import TemplateLoader,\
    TemplateNotFound, TemplateSyntaxError


class credit_transfer_config(osv.Model):
    _name = "account_credit_transfer.config"

    _columns = {
        "bank_id": fields.many2one(
            "res.partner.bank",
            string="Bank",
            ondelete="set null",
        ),
        "parser_id": fields.many2one(
            "account_credit_transfer.parser",
            string="obj",
            ondelete="set null",
        ),
    }

    def get_credit_transfer_file(self, cr, uid, data, context=None):
        parser_osv = self.pool.get("account_credit_transfer.parser")

        config_id = self.search(
            cr, uid,
            [('bank_id', '=', data['debtor_bank'])],
            context=context,
        )
        config = self.browse(cr, uid, config_id, context=context)
        parser = parser_osv.get_parser(cr, uid, config.parser_id, context=context)
        parser.parse(config.parser_id.template)

