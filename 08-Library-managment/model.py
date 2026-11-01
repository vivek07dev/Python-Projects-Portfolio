from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title
        self._available = True

    @property
    def available(self):
        return self._available

    @property
    def is_lendable(self):
        return True

    def mark_borrowed(self):
        self._available = False

    def mark_returned(self):
        self._available = True

    @abstractmethod
    def loan_period_days(self):
        pass


class Book(LibraryItem):
    def loan_period_days(self):
        return 14


class Magazine(LibraryItem):
    def loan_period_days(self):
        return 7


class ReferenceBook(LibraryItem):
    def loan_period_days(self):
        return 0

    @property
    def is_lendable(self):
        return False

class Member:
    max_active_loans_default = 3

    def __init__(self, member_id, name, borrowing_limit=None):
        self.member_id = member_id
        self.name = name
        if borrowing_limit is None:
            borrowing_limit = Member.max_active_loans_default
        self.borrowing_limit = borrowing_limit
        self._active_loans = []

    @property
    def active_loans(self):
        return tuple(self._active_loans)

    @property
    def borrowed_count(self):
        return len(self._active_loans)

    def can_borrow(self):
        return self.borrowed_count < self.borrowing_limit

    def add_loan(self, item_id):
        self._active_loans.append(item_id)

    def remove_loan(self, item_id):
        if item_id in self._active_loans:
            self._active_loans.remove(item_id)

    @classmethod
    def set_default_limit(cls, limit):
        if limit < 1:
            raise ValueError("Limit must be at least 1.")
        cls.max_active_loans_default = limit

class StudentMember(Member):
    def __init__(self, member_id, name, borrowing_limit=3):
        super().__init__(member_id, name, borrowing_limit)

class ResearchStudent(StudentMember):
    def __init__(self, member_id, name, borrowing_limit=5):
        super().__init__(member_id, name, borrowing_limit)

class FacultyMember(Member):
    def __init__(self, member_id, name, borrowing_limit=5):
        super().__init__(member_id, name, borrowing_limit)

class NotificationMixin:
    def send_notice(self, message):
        print("Notice for", self.name + ":", message)

# MRO: NotifiedMember -> Member -> NotificationMixin -> object
class NotifiedMember(Member, NotificationMixin):
    def __init__(self, member_id, name, borrowing_limit=3):
        super().__init__(member_id, name, borrowing_limit)