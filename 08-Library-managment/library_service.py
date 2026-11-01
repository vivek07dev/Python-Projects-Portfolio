from datetime import date, timedelta
from model import Book, Magazine, ReferenceBook, StudentMember, ResearchStudent, FacultyMember, NotifiedMember


class LibraryManager:
    library_name = "City Central Library"

    def __init__(self):
        self.catalogue = {}
        self.members = {}
        self.loans = {}

    def register_item(self, item):
        if item.item_id in self.catalogue:
            raise ValueError("Item ID already exists.")
        self.catalogue[item.item_id] = item

    def register_member(self, member):
        if member.member_id in self.members:
            raise ValueError("Member ID already exists.")
        self.members[member.member_id] = member

    def borrow_item(self, member_id, item_id):
        if member_id not in self.members:
            raise ValueError("Member not found.")
        if item_id not in self.catalogue:
            raise ValueError("Item not found.")

        member = self.members[member_id]
        item = self.catalogue[item_id]

        if not item.available:
            raise ValueError("Item is already borrowed.")
        if not item.is_lendable:
            raise ValueError("Reference books cannot be borrowed.")
        if not member.can_borrow():
            raise ValueError("Borrowing limit exceeded.")

        issue_date = date.today()
        due_date = issue_date + timedelta(days=item.loan_period_days())

        self.loans[item_id] = {
            "item_id": item_id,
            "member_id": member_id,
            "issue_date": issue_date.isoformat(),
            "due_date": due_date.isoformat(),
            "return_date": None
        }

        item.mark_borrowed()
        member.add_loan(item_id)

        if isinstance(member, NotifiedMember):
            member.send_notice("Item " + item_id + " borrowed successfully.")

        return due_date

    @staticmethod
    def calculate_fine(overdue_days, fine_per_day=5):
        return max(0, overdue_days) * fine_per_day

    def return_item(self, item_id):
        if item_id not in self.loans:
            raise ValueError("Loan record not found.")

        loan = self.loans[item_id]

        if loan["return_date"] is not None:
            raise ValueError("Item has already been returned.")

        item = self.catalogue[item_id]
        member = self.members[loan["member_id"]]

        today = date.today()
        due_date = date.fromisoformat(loan["due_date"])
        overdue_days = max(0, (today - due_date).days)
        fine = self.calculate_fine(overdue_days)

        loan["return_date"] = today.isoformat()
        item.mark_returned()
        member.remove_loan(item_id)

        return overdue_days, fine

    @classmethod
    def set_library_name(cls, name):
        cls.library_name = name

    def display_reports(self):
        print("\nLibrary:", self.library_name)

        print("\nAll Items:")
        for item_id, item in self.catalogue.items():
            print(item_id, "|", item.title, "| Available:", item.available)

        print("\nAvailable Items:")
        for item_id, item in self.catalogue.items():
            if item.available:
                print(item_id, "|", item.title)

        print("\nActive Loans:")
        for item_id, loan in self.loans.items():
            if loan["return_date"] is None:
                print(item_id, "|", loan["member_id"], "| Due:", loan["due_date"])

        print("\nOverdue Loans:")
        today = date.today()
        found = False

        for item_id, loan in self.loans.items():
            if loan["return_date"] is None:
                due_date = date.fromisoformat(loan["due_date"])
                if today > due_date:
                    found = True
                    days = (today - due_date).days
                    fine = self.calculate_fine(days)
                    print(item_id, "| Days:", days, "| Fine:", fine)

        if not found:
            print("No overdue loans.")

        print("\nMembers:")
        for member_id, member in self.members.items():
            print(member_id, "|", member.name, "| Borrowed:", member.borrowed_count)