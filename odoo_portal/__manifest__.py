# -*- coding: utf-8 -*-
###############################################################################
#
#    Employee Portal
#    Copyright (C) 2025 Odoo Box
#
###############################################################################

{
    'name': 'Employee Portal',
    'summary': """Employee Self-Service Portal - HR Portal Access Control & Employee Dashboard""",
    'description': """
Employee Portal & Self-Service Module for Odoo 18

Transform your HR management with a comprehensive employee self-service portal that empowers your workforce while reducing HR administrative burden. This professional-grade module extends Odoo's portal functionality to provide employees with secure, intuitive access to their personal information, leave requests, attendance records, payroll details, and more.

🎯 KEY FEATURES:

✅ Employee Self-Service Portal
   - Secure portal access for employees without full Odoo system access
   - Personalized employee dashboard with quick access to key information
   - Modern, responsive design optimized for desktop and mobile devices

✅ Profile Management
   - Employees can view and update their personal information
   - Upload and manage work permits and important documents
   - Real-time profile updates with instant validation

✅ Leave Management Integration
   - Submit leave requests directly from the portal
   - View leave balance and history
   - Track pending approvals and leave calendar
   - Integration with Odoo HR Holidays module

✅ Attendance Tracking
   - View attendance records and timesheets
   - Access attendance history and reports
   - Integration with Odoo HR Attendance module

✅ Payroll Information Access
   - View payslips and salary information
   - Access payroll history and documents
   - Secure access to financial information
   - Integration with Odoo HR Payroll module

✅ Calendar Integration
   - View personal calendar events
   - Access scheduled meetings and appointments
   - Integration with Odoo Calendar module

✅ Security & Access Control
   - Role-based access control (RBAC)
   - Secure portal user type implementation
   - Data privacy and GDPR compliance
   - Customizable security groups and permissions

✅ User Experience
   - Intuitive navigation and user-friendly interface
   - Mobile-responsive design
   - Fast loading times and optimized performance
   - Multi-language support ready

🔧 TECHNICAL SPECIFICATIONS:

- Compatible with Odoo 18.0
- Extends: res.users, hr.employee, portal module
- Dependencies: base, portal, hr, hr_holidays, hr_attendance, hr_payroll, website, calendar
- License: LGPL-3 (Open Source)
- Fully integrated with Odoo's standard HR modules

💼 PERFECT FOR:

- Small to large businesses managing employee self-service
- HR departments seeking to reduce administrative workload
- Companies requiring secure employee data access
- Organizations implementing digital HR transformation
- Businesses needing employee portal functionality without full Odoo access

📈 BENEFITS:

💰 SIGNIFICANT COST SAVINGS - REDUCE ODOO SH USER LICENSES
   - **MAIN BENEFIT**: Eliminate the need to purchase expensive internal Odoo users for employees
   - This module introduces a new "Portal Employee User" type that provides full employee portal functionality
   - Employees can access their HR information, submit leave requests, view payslips, and manage their profile WITHOUT requiring a paid Odoo internal user license
   - Perfect for Odoo.sh customers: Convert expensive internal users to free portal employee users
   - Save thousands of dollars annually on user licensing costs while maintaining full employee self-service capabilities
   - Example: If you have 50 employees, instead of purchasing 50 internal user licenses, use portal employee users at no additional cost!

- Reduce HR administrative tasks by up to 40%
- Improve employee satisfaction with self-service capabilities
- Enhance data accuracy through employee self-updates
- Streamline leave and attendance management
- Provide 24/7 access to employee information
- Maintain security and compliance standards
- No additional user license costs for employee portal access

🔍 SEO KEYWORDS:
employee portal, HR portal, employee self-service, Odoo employee portal, HR management, employee dashboard, leave management, attendance portal, payroll portal, employee access control, HR self-service, portal access, employee profile, Odoo HR, human resources portal, employee management system, self-service HR, employee information portal, Odoo 18 portal, HR automation, employee data access, portal user type, employee portal module, Odoo apps, HR software, employee portal solution

📞 SUPPORT:

For support, documentation, and updates, visit: https://www.odoobox.com

Transform your HR operations today with the Employee Portal & Self-Service Module!
""",
    'author': "Odoo Box",
    'website': 'https://www.odoobox.com',
    'category': 'Portal',
    'version': '18.0.1.0.0',
    'depends': ['base', 'portal', 'hr', 'hr_holidays', 'hr_attendance', 'hr_payroll', 'website', 'calendar'],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_leave_security.xml',
        'data/res_groups_data.xml',
        'views/employee_portal_templates.xml',
        'views/res_users_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'images': ['static/description/portal_menu.png', 'static/description/icon.png', 'static/description/employee_portal_access.png'],
    'license': 'LGPL-3',
    'price': 39.0,
    'currency': 'USD',
}
