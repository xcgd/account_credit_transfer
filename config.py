from openerp.osv import fields, osv
from openerp.tools.translate import _


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
            string="Parser",
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
        voucher_wizards = data['list_voucher_wizard']
        if not all(vw.partner_bank_id.acc_number for vw in voucher_wizards):
            raise osv.except_osv(
                _(u"Error"),
                _(u"Cannot create SEPA batch: no IBAN number.")
            )
        if not configs:
            raise osv.except_osv(
                _('Config Error'),
                _('No config found for this bank. Please set one.'),
            )
        parser = parser_osv.get_parser(
            cr, uid, configs[0].parser_id, context=context)

        print parser

        att_values = parser.compute(configs[0].parser_id.template, data)

        print att_values

        ir_attachment_osv = self.pool.get('ir.attachment')
        ir_attachment_osv.create(cr, uid, att_values, context=context)

#         filename = 'FormirisSEPA'
#
#         file_exists = self.pool[
#             'document_attachment.type'
#             ].search(cr, uid, [
#                 '&', ('name', '=', filename), ('model', '=', self._name)
#             ], context=context
#         )
#
#         if not file_exists:
#             type = self.pool[
#                 'document_attachment.type'
#                 ].create(cr, uid, {
#                     'name': filename,
#                     'model': self._name,
#                 }, context=context
#             )
#         else:
#             for file in file_exists:
#                 type = file
#                 break
#
#         cf_id = config_id[0]
#
#         context['res_model'] = self._name
#         context['res_id'] = cf_id
#
#         print context
#
#         doc = self.pool['document_attachment'].create(
#             cr, uid, att_values, context=context
#         )
