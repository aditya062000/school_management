from odoo import fields, models, api


class SchoolProfile(models.Model):
    _name = 'school.profile'
    _rec_name = 'name'

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    is_virtual_class = fields.Boolean(string="Virtual Class Support?..")
    school_rank = fields.Integer(string="School Rank")
    result = fields.Float(string="Result")
    address = fields.Text(string="Address")
    est_date = fields.Date(string="Establish Date")
    open_date = fields.Datetime(string="Opening Date")
    school_type = fields.Selection([('public','Public'),
                                    ('private','Private')],string='Type of School')
    documents = fields.Binary(string="Documents")

    student_ids = fields.One2many('student.info.line', 'student_id', 'Students')

    # def on_name(self):
    #     for rec in self:
    #         print(rec.student_ids)
    #         # if rec.name == rec.student_ids:
    #         #     print(student.details)


#
class StudentInfoLine(models.Model):
    _name = 'student.info.line'
    # _rec_name = 's_name'

    student_detail_id = fields.Many2one('student.details','Select Student')
    student_email = fields.Char(related='student_detail_id.student_email', string="Email")
    student_phone = fields.Char(related='student_detail_id.student_phone', string="Phone")
    student_address = fields.Char(related='student_detail_id.student_address', string="Address")
    student_id = fields.Many2one('school.profile', 'Student Id')






