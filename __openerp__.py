# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Mariano Ruiz <mrsarm@gmail.com>
#    Enterprise Objects Consulting (<http://www.eoconsulting.com.ar>).
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
##############################################################################


{
    'name': 'Stock Move hide Pack field',
    'version': '1.0',
    'category': 'Warehouse Management',
    'description': """Hides pack field (Tracking Number) from stock move view.""",
    'author': 'Enterprise Objects Consulting',
    'website': 'http://www.eoconsulting.com.ar',
    'depends': ['stock'],
    'init_xml': [],
    'update_xml': ['stock_move_hide_pack_view.xml',],
    'demo_xml': [],
    'test':[],
    'installable': True,
    'active': False,
}
