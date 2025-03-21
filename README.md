# پروژه وب‌سایت بررسی اطلاعات GitHub  

این پروژه یک وب‌سایت ساده است که به کاربران این امکان را می‌دهد تا آمار و اطلاعات مربوط به فعالیت‌های خود در GitHub را بررسی کنند. با استفاده از این وب‌سایت، کاربران می‌توانند نام کاربری GitHub خود را وارد کرده و به اطلاعاتی از قبیل آمار کلی و زبان‌های برنامه‌نویسی مورد استفاده دسترسی پیدا کنند.  

## ⚙️ تکنولوژی‌های استفاده شده  

- **Flask**: برای ایجاد سرور و مدیریت درخواست‌ها  
- **Requests**: برای ارسال درخواست به API گیت‌هاب  
- **HTML & CSS**: برای طراحی فرانت‌اند وب‌سایت  

## 📑 عملکرد کد  

### 1. بررسی اعتبار نام کاربری GitHub  
با استفاده از تابع `is_valid_github_username(username)`، اعتبار نام کاربری GitHub بررسی می‌شود. این تابع به API گیت‌هاب درخواست ارسال کرده و در صورت دریافت کد وضعیت 200 (موفق) نتیجه می‌گیرد که نام کاربری معتبر است.  

### 2. صفحات وب  
- **صفحه اصلی (`/`)**: کاربر می‌تواند نام کاربری GitHub خود را وارد کند. در صورت معتبر بودن نام کاربری، آمار و اطلاعات مربوط به آن در صفحه جدیدی نمایش داده می‌شود.  
- **صفحه آمار (`stats.html`)**: در این صفحه آمار و اطلاعات مربوط به نام کاربری شامل تصویر آمار، تصویر زبان‌های برنامه‌نویسی و یک انیمیشن نمایش داده می‌شود.  

## 🌟 تصاویری که نمایش داده می‌شود  

1. **آمار کلی**: با استفاده از API گیت‌هاب، آمار کاربران شامل تعداد ریپوزیتوری‌ها، تعداد کامیت‌ها و دیگر اطلاعات در موضوع `radical` نمایش داده می‌شود.  
   
2. **زبان‌های برنامه‌نویسی**: تصویر زبان‌های برنامه‌نویسی استفاده شده توسط کاربر نیز به نمایش درمی‌آید.  

3. **انیمیشن**: یک انیمیشن زیبا از فعالیت‌های کاربر بر روی گیت‌هاب نمایش داده می‌شود.  

## 📦 نحوه راه‌اندازی  

1. **نصب وابستگی‌ها**:  
   ```bash  
   pip install Flask requests  
