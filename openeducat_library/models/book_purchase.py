# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import models, fields, api


class OpBookPurchase(models.Model):
    _name = 'op.book.purchase'

    name = fields.Char('Title', size=128, required=True)
    author = fields.Char('Author(s)', size=256, required=True)
    edition = fields.Char('Edition')
    publisher = fields.Char('Publisher(s)', size=256)
    course_ids = fields.Many2one('op.course', 'Course', required=True)
    subject_ids = fields.Many2one('op.subject', 'Subject', required=True)
    student_id = fields.Many2one(
        'op.student', 'Student',
        default=lambda self: self.env.user.user_line and
        self.env.user.user_line[0].id or False)
    faculty_id = fields.Many2one('op.faculty', 'Faculty')
    librarian_id = fields.Many2one('res.partner', 'Librarian')
    state = fields.Selection(
        [('draft', 'Draft'), ('request', 'Requested'), ('accept', 'Accepted'),
         ('reject', 'Rejected')], 'State', select=True, readonly=True,
        default='draft')

    @api.one
    def act_requested(self):
        self.state = 'request'

    @api.one
    def act_accept(self):
        self.state = 'accept'

    @api.one
    def act_reject(self):
        self.state = 'reject'


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
