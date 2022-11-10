# -*- coding: utf-8 -*-

from odoo import models, fields, api

from random import randint

class RepairHerencia(models.Model): 
    _name = 'repair.order'
    _inherit = 'repair.order'

    accesorios = fields.Char()
    numero_de_serie = fields.Char(string='Número de serie')
    observaciones = fields.Text()
    tipo_de_falla = fields.Many2many('mundotec.tdf.tags', string="Tipo de falla")
    marca = fields.Many2one('mundotec.marca', string='Marca')
    modelo = fields.Many2one('mundotec.modelo', string='Modelo')
    subestatus = fields.Many2one('mundotec.subestatus', string='Sub estatus')
    user_id = fields.Many2one('res.users', string="Técnico", default=lambda self: self.env.user, check_company=True)
    recibido_por = fields.Many2one('res.users', string="Recibido por", check_company=True)
    
class RepairLineHer(models.Model):
    _name = 'repair.line'
    _inherit = 'repair.line'

    product_id = fields.Many2one(
        'product.product', 'Product', required=True, check_company=True,
        domain="[('categ_id', 'like', 'CELULAR')]")

class TipoFallaTags(models.Model):
    _name = "mundotec.tdf.tags"
    _description = "Tipo de Falla Tags"

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char('Tag Name', required=True)
    color = fields.Integer(string='Color Index', default=_get_default_color)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Nombre de Tag ya existe!"),
    ]

class Marca(models.Model):
    _name = "mundotec.marca"
    _description = "Marca"

    name = fields.Char(string="Marca")

class Modelo(models.Model):
    _name = "mundotec.modelo"
    _description = "mundotec.modelo"

    name = fields.Char(string="Modelo")

class Subestatus(models.Model):
    _name = "mundotec.subestatus"
    _description = "Subestatus"

    name = fields.Char(string="Sub estatus")

