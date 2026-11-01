import json
import os
from model import Book, Magazine, ReferenceBook, StudentMember, ResearchStudent, FacultyMember, NotifiedMember


def save_library(manager, file_path="data.json"):
    data = {
        "items": [],
        "members": [],
        "loans": manager.loans
    }

    for item in manager.catalogue.values():
        data["items"].append({
            "type": type(item).__name__,
            "item_id": item.item_id,
            "title": item.title,
            "available": item.available
        })

    for member in manager.members.values():
        data["members"].append({
            "type": type(member).__name__,
            "member_id": member.member_id,
            "name": member.name,
            "borrowing_limit": member.borrowing_limit,
            "active_loans": list(member.active_loans)
        })

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_library(manager, file_path="data.json"):
    if not os.path.exists(file_path):
        return manager

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("Invalid library data.")

    item_classes = {
        "Book": Book,
        "Magazine": Magazine,
        "ReferenceBook": ReferenceBook
    }

    member_classes = {
        "StudentMember": StudentMember,
        "ResearchStudent": ResearchStudent,
        "FacultyMember": FacultyMember,
        "NotifiedMember": NotifiedMember
    }

    for saved_item in data["items"]:
        item_type = saved_item["type"]

        if item_type not in item_classes:
            raise ValueError("Unknown item type.")

        item = item_classes[item_type](
            saved_item["item_id"],
            saved_item["title"]
        )

        if saved_item["available"] is False:
            item.mark_borrowed()

        manager.register_item(item)

    for saved_member in data["members"]:
        member_type = saved_member["type"]

        if member_type not in member_classes:
            raise ValueError("Unknown member type.")

        member = member_classes[member_type](
            saved_member["member_id"],
            saved_member["name"],
            saved_member["borrowing_limit"]
        )

        for item_id in saved_member["active_loans"]:
            member.add_loan(item_id)

        manager.register_member(member)

    manager.loans = data["loans"]
    return manager