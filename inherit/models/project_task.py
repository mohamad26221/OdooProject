from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    progress_percentage = fields.Float(
        string='Progress Percentage',
        compute='_compute_task_progress_percentage',
        store=True
    )

    @api.depends('planned_hours', 'effective_hours')
    def _compute_task_progress_percentage(self):
        for task in self:
            if task.planned_hours > 0:
                task.progress_percentage = (task.effective_hours / task.planned_hours) * 100
            else:
                task.progress_percentage = 0
