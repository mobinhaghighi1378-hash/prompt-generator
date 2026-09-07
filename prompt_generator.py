#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
برنامه تولید پرامپت حرفه‌ای برای مدل‌های هوش مصنوعی
Prompt Generator for AI Models
"""

import os
from typing import Dict, List
from enum import Enum

class Style(Enum):
    """استایل پرامپت"""
    FORMAL = "رسمی و حرفه‌ای"
    FRIENDLY = "دوستانه و گرم"
    CREATIVE = "خلاقانه و تخیلی"
    TECHNICAL = "تکنیکی و دقیق"

class AudienceLevel(Enum):
    """سطح دانش مخاطب"""
    BEGINNER = "تازه‌کار"
    INTERMEDIATE = "متوسط"
    ADVANCED = "پیشرفته"
    EXPERT = "متخصص"

class Purpose(Enum):
    """هدف از پرامپت"""
    LEARNING = "یادگیری و آموزش"
    WORK = "کار و تولید محتوا"
    ANALYSIS = "تحلیل و بررسی"
    CREATIVITY = "خلاقیت و ایده‌پردازی"
    PROBLEM_SOLVING = "حل مسئله"

class PromptGenerator:
    def __init__(self):
        self.topic = ""
        self.style = None
        self.audience = None
        self.purpose = None
        self.additional_context = ""

    def get_topic(self) -> str:
        """دریافت موضوع از کاربر"""
        print("\n" + "="*60)
        print("🎯 خوش‌آمدید به برنامه تولید پرامپت حرفه‌ای!")
        print("="*60)
        print("\n📝 لطفاً موضوع یا مسئله‌ای را که می‌خواهید پرامپت برای آن تولید کنید، وارد کنید:")
        print("(مثال: 'یک متن توضیحی برای یادگیری Python' یا 'نوشتن یک داستان علمی‌تخیلی')\n")
        
        topic = input("📌 موضوع: ").strip()
        
        if not topic:
            print("❌ موضوع نمی‌تواند خالی باشد!")
            return self.get_topic()
        
        self.topic = topic
        return topic

    def select_style(self) -> Style:
        """انتخاب استایل پرامپت"""
        print("\n" + "-"*60)
        print("🎨 استایل پرامپت را انتخاب کنید:")
        print("-"*60)
        
        styles = list(Style)
        for i, style in enumerate(styles, 1):
            print(f"{i}. {style.value}")
        
        while True:
            try:
                choice = int(input("\n👉 انتخاب کنید (عدد): ").strip())
                if 1 <= choice <= len(styles):
                    self.style = styles[choice - 1]
                    print(f"✅ انتخاب شد: {self.style.value}")
                    return self.style
                else:
                    print(f"❌ لطفاً عددی بین 1 و {len(styles)} وارد کنید!")
            except ValueError:
                print("❌ لطفاً یک عدد درست وارد کنید!")

    def select_audience(self) -> AudienceLevel:
        """انتخاب سطح دانش مخاطب"""
        print("\n" + "-"*60)
        print("👥 سطح دانش مخاطب را انتخاب کنید:")
        print("-"*60)
        
        audiences = list(AudienceLevel)
        for i, audience in enumerate(audiences, 1):
            print(f"{i}. {audience.value}")
        
        while True:
            try:
                choice = int(input("\n👉 انتخاب کنید (عدد): ").strip())
                if 1 <= choice <= len(audiences):
                    self.audience = audiences[choice - 1]
                    print(f"✅ انتخاب شد: {self.audience.value}")
                    return self.audience
                else:
                    print(f"❌ لطفاً عددی بین 1 و {len(audiences)} وارد کنید!")
            except ValueError:
                print("❌ لطفاً یک عدد درست وارد کنید!")

    def select_purpose(self) -> Purpose:
        """انتخاب هدف از پرامپت"""
        print("\n" + "-"*60)
        print("🎯 هدف از این پرامپت چیست؟")
        print("-"*60)
        
        purposes = list(Purpose)
        for i, purpose in enumerate(purposes, 1):
            print(f"{i}. {purpose.value}")
        
        while True:
            try:
                choice = int(input("\n👉 انتخاب کنید (عدد): ").strip())
                if 1 <= choice <= len(purposes):
                    self.purpose = purposes[choice - 1]
                    print(f"✅ انتخاب شد: {self.purpose.value}")
                    return self.purpose
                else:
                    print(f"❌ لطفاً عددی بین 1 و {len(purposes)} وارد کنید!")
            except ValueError:
                print("❌ لطفاً یک عدد درست وارد کنید!")

    def get_additional_context(self) -> str:
        """دریافت اطلاعات اضافی اختیاری"""
        print("\n" + "-"*60)
        print("📋 اطلاعات اضافی (اختیاری):")
        print("-"*60)
        print("اگر اطلاعات اضافی‌ای درباره موضوع دارید، وارد کنید.")
        print("(اگر نه، فقط Enter را فشار دهید)\n")
        
        context = input("📝 اطلاعات اضافی: ").strip()
        self.additional_context = context
        return context

    def generate_prompt(self) -> str:
        """تولید پرامپت حرفه‌ای"""
        print("\n" + "="*60)
        print("✨ تولید پرامپت...")
        print("="*60 + "\n")

        style_desc = self.style.value
        audience_desc = self.audience.value
        purpose_desc = self.purpose.value
        
        prompt_template = f"""تو یک دستیار هوش‌مصنوعی ماهر و حرفه‌ای هستی.

📌 **موضوع:**
{self.topic}

🎨 **استایل ارائه:**
{style_desc}

👥 **مخاطب:**
{audience_desc}

🎯 **هدف:**
{purpose_desc}
"""
        
        if self.additional_context:
            prompt_template += f"\n📋 **اطلاعات اضافی:**\n{self.additional_context}"
        
        prompt_template += f"""

🔹 **نکات مهم:**
- پاسخ خود را بر اساس استایل و سطح مخاطب سفارشی کنید
- از مثال‌ها و توضیحات استفاده کنید
- پاسخ خود را واضح و ساختار‌یافته ارائه دهید
- از تصویرسازی ذهنی و نمونه‌های عملی استفاده کنید

حالا به سؤال یا درخواست من پاسخ دهید:
"""
        
        return prompt_template

    def run(self):
        """اجرای برنامه"""
        try:
            # مراحل انتخاب
            self.get_topic()
            self.select_style()
            self.select_audience()
            self.select_purpose()
            self.get_additional_context()
            
            # تولید پرامپت
            generated_prompt = self.generate_prompt()
            
            # نمایش پرامپت
            print("="*60)
            print("📄 پرامپت تولید شده:")
            print("="*60)
            print(generated_prompt)
            print("\n" + "="*60)
            
            # ذخیره پرامپت
            self.save_prompt(generated_prompt)
            
            # پیشنهاد ادامه
            self.ask_continue()
            
        except KeyboardInterrupt:
            print("\n\n👋 برنامه بسته شد. خداحافظ!")
        except Exception as e:
            print(f"\n❌ خطای غیرمنتظره: {e}")

    def save_prompt(self, prompt: str):
        """ذخیره پرامپت در فایل"""
        print("\n💾 آیا می‌خواهید این پرامپت را ذخیره کنید؟ (y/n)")
        choice = input("👉 ").strip().lower()
        
        if choice == 'y':
            filename = f"prompt_{len(self.topic.split())}_words.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"موضوع: {self.topic}\n")
                f.write(f"استایل: {self.style.value}\n")
                f.write(f"مخاطب: {self.audience.value}\n")
                f.write(f"هدف: {self.purpose.value}\n")
                f.write("="*60 + "\n\n")
                f.write(prompt)
            print(f"✅ ذخیره شد: {filename}")

    def ask_continue(self):
        """پرسیدن برای ادامه"""
        print("\n🔄 آیا می‌خواهید پرامپت دیگری تولید کنید؟ (y/n)")
        choice = input("👉 ").strip().lower()
        
        if choice == 'y':
            # بازنشانی متغیرها
            self.__init__()
            self.run()
        else:
            print("\n👋 متشکرم! برنامه بسته شد.")

def main():
    """تابع اصلی"""
    generator = PromptGenerator()
    generator.run()

if __name__ == "__main__":
    main()
