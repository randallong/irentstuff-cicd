It is important to understand how models and modules are connected to understand how testing works.

**Models**
Category - No dependencies
Item - Depends on Category
Message - Depends on Item
Rental - Depends on Item
Review - Depends on Rental

**Modules**
User interaction --> urls --> views --> forms --> models

**Testing flow**
1. Test scripts must start with `test_`
2. Tests are written as TestCase classes, which inherit from django.test.TestCase
3. The first step in a TestCase is to set up the required objects. This is done as the first method in the class, defined as setUp(self).
4. 
