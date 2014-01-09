from openerp.osv import fields, osv


class credit_transfer_config(osv.Model):
    _name = "account_credit_transfer.config"

    _columns = {
        "bank_id": fields.many2one(
            "res.bank",
            string="Bank",
            ondelete="set null",
        ),
        "parser_id": fields.many2one(
            "account_credit_transfer.parser",
            string="obj",
            ondelete="set null",
        ),
    }

    def generate_credit_transfer_file(self, cr, uid, data, context=None):
        parser_osv = self.pool.get("account_credit_transfer.parser")

        config_id = self.search(
            cr, uid,
            [('bank_id', '=', data['debtor_bank'].bank.id)],
            context=context,
        )
        configs = self.browse(cr, uid, config_id, context=context)
        if not configs:
            raise osv.except_osv(
                _('Config Error'),
                _('No config found for this bank. Please set one.'),
            )
        parser = parser_osv.get_parser(
            cr, uid, config.parser_id, context=context)
        att_values = parser.compute(config.parser_id.template, data)
        ir_attachment_osv = self.pool.get('ir.attachment')
        ir_attachment_osv.create(cr, uid, att_values, context=context)


