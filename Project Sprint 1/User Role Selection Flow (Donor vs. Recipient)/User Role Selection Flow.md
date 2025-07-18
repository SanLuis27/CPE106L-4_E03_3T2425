# RePlate: User Role Selection Flow  
**Task:** User Role Selection Flow (Donor vs. Recipient)  
**Sprint Week:** 1  
**Assigned To:** Miguel San Luis  
**Date Started:** July 11, 2025  
**Target Completion:** July 13, 2025  

---

## 🎯 Objective  
Allow users to choose their role—**Donor** or **Recipient**—during login. This determines their available features and dashboard flow.

---

## 🧩 User Flow Steps

1. **Open App → Home Screen**  
   - Welcome message with two options:  
     **[1] Donor**  
     **[2] Recipient**

2. **User Makes Selection**  
   - App sets user role in session (e.g., `user_role = "Donor"`)

3. **Redirect to Login/Register Form**  
   - Authentication is initiated post-role selection

4. **Post Login:**  
   - If `Donor`, show menu:  
     - Add new donation  
     - View past donations  
   - If `Recipient`, show menu:  
     - Request food  
     - Track delivery

5. **Session Maintains Role**  
   - App navigation and features adjust based on `user_role` throughout session

---
