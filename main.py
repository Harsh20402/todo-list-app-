import time

class ToDoList:
    def __init__(self, user_name):
        self.user_name = user_name
        self.to_do_list_items = []

    def run(self):
        print(f"\n🎉 Welcome, {self.user_name}! Let's build your To-Do List 🚀\n")

        while True:
            choice = self.check_user_choice()
            print(f"\n📌 Your Choice: {self.option_display(choice)}\n")

            if choice == 1:
                self.add_item()
            elif choice == 2:
                self.view_items()
            elif choice == 3:
                self.update_item()
            elif choice == 4:
                self.delete_item()
            elif choice == 5:
                self.exit()
                break

    @staticmethod
    def show_menu():
        print("""
        📌 What would you like to do?
                
         1️⃣  Add New Item.
         2️⃣  View Items.
         3️⃣  Update Item.
         4️⃣  Delete Item.
         5️⃣  Exit.
        """)

    def option_display(self, choice):
        return {
            1: "➕ Add New Item.",
            2: "👀 View Items.",
            3: "✏️ Update Item.",
            4: "🗑️ Delete Item.",
            5: "👋 Exit."
        }.get(choice, "❓ Unknown Option")

    def check_user_choice(self):
        while True:
            self.show_menu()
            user_input = input(f"👋 Hey {self.user_name}, enter your choice (1-5): ").strip()

            if user_input.isdigit():
                final_choice = int(user_input)
                if self.final_check_user_input(final_choice):
                    return final_choice
            print("⚠️ Invalid input. Please enter a number between 1 and 5.")

    def final_check_user_input(self, choice):
        if 1 <= choice <= 5:
            return True
        else:
            print(f"⚠️ {self.user_name}, please choose a valid option (1 to 5).")
            return False

    def add_item(self):
        item = input("🆕 Enter the new item to add: ").strip().capitalize()
        print("⏳ Under Processing...")
        time.sleep(1)

        if item:
            self.to_do_list_items.append(item)
            print(f"📝 Updated To-Do List: 📝 {' | '.join(self.to_do_list_items)}\n")
        else:
            print("⚠️ Item cannot be empty.\n")

    def view_items(self):
        print("⏳ Loading...")
        time.sleep(1)

        if self.to_do_list_items:
            print("📄 Your To-Do List:")
            for i, item in enumerate(self.to_do_list_items, 1):
                print(f"  {i}. {item}")
            print()
        else:
            print(f"⚠️ {self.user_name}, there is no item present in your To-Do List.\n")

    def update_item(self):
        item_name = input("✏️ Enter the item you want to update: ").strip().capitalize()
        print("⏳ Update is in progress...")
        time.sleep(1)

        if item_name in self.to_do_list_items:
            new_name = input("🔄 Enter the new item name: ").strip().capitalize()
            if new_name:
                index = self.to_do_list_items.index(item_name)
                self.to_do_list_items[index] = new_name
                print(f"✅ Item '{item_name}' updated to '{new_name}'.\n")
            else:
                print("⚠️ New item name cannot be empty.\n")
        else:
            print(f"❌ Item '{item_name}' not found in the list.\n")

    def delete_item(self):
        item_name = input("🗑️ Enter the item you want to delete: ").strip().capitalize()
        print("⏳ Under Processing...")
        time.sleep(1)

        if item_name in self.to_do_list_items:
            self.to_do_list_items.remove(item_name)
            print(f"✅ Item '{item_name}' has been deleted.\n")
        else:
            print(f"❌ Item '{item_name}' not found in the list.\n")

    def exit(self):
        print(f"\n👋 Goodbye, {self.user_name}! Final To-Do List:")
        if not self.to_do_list_items:
            print("🈳 Your list is empty.")
        else:
            for i, item in enumerate(self.to_do_list_items, 1):
                print(f"  {i}. {item}")
        print()

def main():
    user_name = input("🙋 What's Your Name: ").strip().capitalize()
    app = ToDoList(user_name)
    app.run()

if __name__ == "__main__":
    main()
