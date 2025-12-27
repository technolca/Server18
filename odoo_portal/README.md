# Employee Portal

[![Odoo Version](https://img.shields.io/badge/Odoo-18.0-blue.svg)](https://www.odoo.com)
[![License](https://img.shields.io/badge/License-LGPL--3-green.svg)](LICENSE)

**Employee Portal** is an Odoo 18 module that provides comprehensive employee self-service portal functionality. It empowers your workforce with secure, intuitive access to their personal information, leave requests, attendance records, payroll details, and more, while significantly reducing HR administrative burden.

## 🎯 Overview

This professional-grade module extends Odoo's portal functionality to provide employees with a complete self-service experience. The module introduces a new "Portal Employee User" type that allows employees to access HR information without requiring expensive internal Odoo user licenses, making it perfect for Odoo.sh customers looking to reduce licensing costs.

## ✨ Features

### Employee Self-Service Portal
- Secure portal access for employees without full Odoo system access
- Personalized employee dashboard with quick access to key information
- Modern, responsive design optimized for desktop and mobile devices
- Intuitive navigation and user-friendly interface

### Profile Management
- Employees can view and update their personal information
- Upload and manage work permits and important documents
- Real-time profile updates with instant validation
- Secure document management

### Leave Management Integration
- Submit leave requests directly from the portal
- View leave balance and history
- Track pending approvals and leave calendar
- Full integration with Odoo HR Holidays module

### Attendance Tracking
- View attendance records and timesheets
- Access attendance history and reports
- Integration with Odoo HR Attendance module
- Real-time attendance data

### Payroll Information Access
- View payslips and salary information
- Access payroll history and documents
- Secure access to financial information
- Integration with Odoo HR Payroll module

### Calendar Integration
- View personal calendar events
- Access scheduled meetings and appointments
- Integration with Odoo Calendar module
- Event management and reminders

### Security & Access Control
- Role-based access control (RBAC)
- Secure portal user type implementation
- Data privacy and GDPR compliance
- Customizable security groups and permissions

## 📋 Requirements

- **Odoo Version:** 18.0
- **Dependencies:**
  - `base`
  - `portal`
  - `hr`
  - `hr_holidays`
  - `hr_attendance`
  - `hr_payroll`
  - `website`
  - `calendar`

## 🚀 Installation

1. Copy the `odoo_portal` folder to your Odoo addons directory
2. Update the apps list in Odoo (Settings → Apps → Update Apps List)
3. Search for "Employee Portal" in the Apps menu
4. Click "Install" to activate the module

## 💰 Cost Savings

### Main Benefit: Reduce Odoo.sh User Licenses

This module introduces a new **"Portal Employee User"** type that provides full employee portal functionality without requiring paid Odoo internal user licenses.

**Key Advantages:**
- Eliminate the need to purchase expensive internal Odoo users for employees
- Employees can access HR information, submit leave requests, view payslips, and manage their profile WITHOUT requiring a paid license
- Perfect for Odoo.sh customers: Convert expensive internal users to free portal employee users
- Save thousands of dollars annually on user licensing costs

**Example:** If you have 50 employees, instead of purchasing 50 internal user licenses, use portal employee users at no additional cost!

## 📖 Usage

### Setting Up Portal Employee Users

1. Navigate to **Settings → Users & Companies → Users**
2. Create a new user or edit an existing user
3. Set the **User Type** to "Employee Portal User"
4. Assign the user to an employee record
5. The user will automatically have access to the employee portal

### Employee Portal Features

Once logged in, employees can:
- View and update their profile information
- Submit leave requests
- View attendance records
- Access payslips and payroll information
- View calendar events
- Manage documents and work permits

## 🔧 Technical Details

### Module Structure

```
odoo_portal/
├── __init__.py
├── __manifest__.py
├── controllers/
│   ├── __init__.py
│   └── employee_portal_controller.py
├── models/
│   ├── __init__.py
│   └── res_users.py
├── views/
│   ├── employee_portal_templates.xml
│   └── res_users_views.xml
├── data/
│   └── res_groups_data.xml
├── security/
│   ├── ir.model.access.csv
│   └── hr_leave_security.xml
└── static/
    └── description/
        └── index.html
```

### Key Components

- **ResUsers Model Extension**: Adds "Employee Portal User" type to user management
- **Employee Portal Controller**: Handles portal routes and access control
- **Portal Templates**: Custom templates for employee portal interface
- **Security Groups**: Defines access control groups for portal users

### API & Integration

The module integrates seamlessly with:
- Odoo HR Holidays module for leave management
- Odoo HR Attendance module for attendance tracking
- Odoo HR Payroll module for payslip access
- Odoo Calendar module for event management
- Odoo Portal module for base portal functionality

## 🎨 Customization

The module can be customized through:
- Custom portal templates in `views/employee_portal_templates.xml`
- Security group modifications in `data/res_groups_data.xml`
- Controller extensions in `controllers/employee_portal_controller.py`

## 🐛 Troubleshooting

### Portal Access Issues
- Ensure the user has "Employee Portal User" type selected
- Verify the user is assigned to an employee record
- Check that the portal group is assigned to the user

### Leave Request Not Showing
- Verify `hr_holidays` module is installed
- Check security groups and access rights
- Ensure employee record is properly linked

### Payroll Information Not Accessible
- Verify `hr_payroll` module is installed
- Check that payslips exist for the employee
- Verify security access rights

## 📝 Changelog

### Version 18.0.1.0.0
- Initial release for Odoo 18.0
- Employee Portal User type implementation
- Integration with HR modules
- Portal dashboard and navigation
- Profile management features
- Leave request functionality
- Attendance tracking integration
- Payroll information access
- Calendar integration

## 👥 Author

**Odoo Box**
- Website: https://www.odoobox.com
- Support: https://www.odoobox.com

## 📄 License

This module is licensed under LGPL-3.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For support, documentation, and updates, visit: https://www.odoobox.com

---

**Transform your HR operations today with the Employee Portal & Self-Service Module!**
