# Part 2: Framework Design

---

## What's Here

```
Part2_Framework_Design/
├── framework_design.md          # How I'd organize the framework
├── folder_structure.txt         # Folder layout
├── missing_requirements.md      # Questions I'd ask
├── config_example.py           # Config code sample
└── base_test_example.py        # Base class code sample
```

---

## Overview

Designed a framework for WorkflowPro that handles:
- Web (Chrome, Firefox, Safari) and Mobile (iOS, Android)
- Multi-tenant (company1, company2)
- User roles (Admin, Manager, Employee)
- API testing
- BrowserStack
- CI/CD

---

## Main Ideas

1. **Page Object Model** - Tests don't have selectors
2. **Config file** - Easy to switch environments
3. **Base classes** - No repeated code
4. **Pytest** - Standard tool

---

## Files

- **framework_design.md** - My framework design
- **folder_structure.txt** - Folder organization
- **missing_requirements.md** - Questions I need answered
- **config_example.py** - Working config code
- **base_test_example.py** - Working base class code

---

**Time:** 25 minutes  
**Result:** Framework design ready for implementation
