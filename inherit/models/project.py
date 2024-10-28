from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'


    task_count = fields.Integer(
        string="Task Count",
        compute='_compute_task_count',
        store=True
    )
    progress_percentage = fields.Float(
        string="Progress Percentage",
        compute='_compute_progress_percentage'
    )
    @api.depends('task_ids')
    def _compute_task_count(self):
        for project in self:
            project.task_count = len(project.task_ids)

    @api.depends('task_ids.stage_id')
    def _compute_progress_percentage(self):
        for project in self:
            total_tasks = len(project.task_ids)
            completed_tasks = len(project.task_ids.filtered(lambda task: task.stage_id.name == 'Done'))
            project.progress_percentage = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0.0

    def action_generate_pdf_report(self):
        return self.env.ref('inherit.project_progress_pdf_report').report_action(self)