from odoo import fields, models, api, _


class StudentDetails(models.Model):
    _name = 'student.details'
    _rec_name = 'student_name'

    student_name = fields.Char(string="Name")
    student_email = fields.Char(string="Email")
    student_phone = fields.Char(string="Phone")
    student_address = fields.Char(string="Address")
    student_school_id = fields.Many2one('school.profile', string='Select School')




    # def create_school(self):
    #     for rec in self:
    #         student_id = self.env['student.details'].create({
    #             'student_name': 'Aditya Nachan',
    #             'student_email': 'aditya@gmail.com',
    #             'student_phone': '987456321',
    #             'student_address': 'Mumbai',
    #             'student_school_id': rec.student_school_id.id,
    #         })
    #         print(student_id)

    # def create_school(self):
    #     for rec in self:
    #         patient_id_search = self.env['student.details'].search(
    #             [('student_school_id', '=', rec.student_school_id.id)])
    #         print(patient_id_search)
    #         for stu in patient_id_search:
    #                 stu.unlink()

    # def create_school(self):
    #     for rec in self:
    #         patient_id_search = self.env['student.details'].search(
    #             [('student_school_id', '=', rec.student_school_id.name)])
    #         patient_id = patient_id_search.write({
    #             'student_name': 'Sachin More',
    #             'student_email': 'sachin@gmail.com',
    #             'student_phone': '987776321',
    #             'student_address': 'Goa',
    #             'student_school_id': rec.student_school_id.id,
    #         })
    #     print(patient_id)
