from collections import defaultdict, OrderedDict


class MeasurementType:
    """
    Class to define measurement types as constants.
    These are used to filter the substrings based on their measurement characteristics.
    """

    ALL = "all"
    NON_CONSTANT = "non_constant"
    ZERO = "zero"
    NON_ZERO = "non_zero"


class TrieNode:
    """
    Class representing a node in the Trie. Each node contains a dictionary of children nodes,
    a flag indicating if it is the end of a word, and a list of strings that pass through this node.
    """

    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False
        self.strings: list[tuple[str, str]] = []


class Trie:
    """
    Trie (prefix tree) for efficient prefix-based searches.
    Supports insertion of strings and searching for strings by prefix.
    """

    def __init__(self):
        self.root: TrieNode = TrieNode()

    def insert(self, word: str, original_string: tuple[str, str]) -> None:
        """
        Inserts a word into the Trie. Each node along the path of the word
        stores the original string associated with the word.

        Args:
            word (str): The word that will be inserted into the trie.
            original_string (tuple[str, str]): The group name and the substring.
        """
        node: TrieNode = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.strings.append(original_string)
        node.is_end_of_word = True

    def search_prefix(self, prefix: str) -> list[tuple[str, str]]:
        """
        Searches for all strings in the Trie that match the given prefix.

        Args:
            prefix (str): The search term.

        Returns:
            list[tuple[str, str]]: List of original strings associated with the matched prefix
        """
        node: TrieNode = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.strings


class GroupStringFilter:
    """
    Class to manage groups of strings and their filtering based on user inputs.
    Supports filtering by substring, group name, and type.
    """

    def __init__(self):
        self.groups: defaultdict[str, list[tuple[str, any]]] = defaultdict(
            list
        )  # Dictionary to store groups and their corresponding (string, type) tuples
        self.display_order: OrderedDict[str:None] = (
            OrderedDict()  # List to maintain the order of group names for display
        )
        self.current_mode: str = (
            "Substring"  # Current filtering mode: "Substring" or "Group"
        )
        self.search_term: str = ""  # Current search term for filtering
        self.filter_type: str = MeasurementType.ALL  # Current filter
        self.trie: Trie = Trie()  # Trie for efficient substring searches

    def add_entries(
        self,
        entries: list[str],
        types: list[any],
        seperator: str,
        sub_header_first: bool = True,
    ) -> None:
        """
        Adds multiple entries from a list of strings and their corresponding types.

        Args:
            entries (list[str]): List of strings.
            types (list[any]): Type of values represented by the string.
            seperator (str): Seperator between group_name and substring.
            sub_header_first (bool, optional): Indicator if the root or the leaf comes first in the texts.
                                                Defaults to True.
        """
        self.groups.clear()
        self.display_order.clear()

        self.trie = Trie()

        for entry, filter_type in zip(entries, types):
            if sub_header_first:
                group_name, substring = entry.split(seperator)
            else:
                substring, group_name = entry.split(seperator)
            group_name = group_name.strip()
            substring = substring.strip()

            self.display_order[group_name] = None

            self.groups[group_name].append((substring, filter_type))
            self.trie.insert(substring.lower(), (group_name, substring))

    def set_mode(self, mode: str) -> None:
        """
        Sets the current filtering mode.
        """
        self.current_mode = mode

    def set_search_term(self, term: str) -> None:
        """
        Sets the current search term for filtering.
        """
        self.search_term = term.lower()

    def set_filter(self, filter_type: str) -> None:
        """
        Sets the current filter.
        """
        self.filter_type = filter_type

    def filter(self) -> list[tuple[str, str, any]]:
        """
        Filters the groups and strings based on the current mode,
        search term, and filter.
        """
        if self.current_mode == "Substring":
            return self.filter_by_substring()
        else:
            return self.filter_by_group()

    def filter_by_type(
        self, items: list[tuple[str, str, any]]
    ) -> list[tuple[str, str, any]]:
        """
        Filters the given items based on the current filter type.
        """
        if self.filter_type == MeasurementType.ALL:
            return items
        elif self.filter_type == MeasurementType.NON_CONSTANT:
            return [(group, s, m) for group, s, m in items if m == "non_constant"]
        elif self.filter_type == MeasurementType.ZERO:
            return [(group, s, m) for group, s, m in items if m == "zero"]
        elif self.filter_type == MeasurementType.NON_ZERO:
            return [(group, s, m) for group, s, m in items if m != "zero"]

    def filter_by_substring(self) -> list[tuple[str, str, any]]:
        """
        Filters the strings by the current search term using the Trie.
        Further filters the results by the current filter type.
        """
        if not self.search_term:
            all_items = [
                (group, s, m)
                for group in list(self.display_order.keys())
                for s, m in self.groups[group]
            ]
            return self.filter_by_type(all_items)

        matching_strings = self.trie.search_prefix(self.search_term)
        all_items = [
            (group, s, m)
            for group, s in matching_strings
            for _, m in self.groups[group]
            if s == _
        ]

        return self.filter_by_type(all_items)

    def filter_by_group(self) -> list[tuple[str, str, any]]:
        """
        Filters the groups by the current search term.
        Further filters the results by the current filter type.
        """
        result = []
        for group in list(self.display_order.keys()):
            if self.search_term in group.lower():
                items = [(group, s, m) for s, m in self.groups[group]]
                result.extend(self.filter_by_type(items))
        return result

    def display(self) -> None:
        """
        Displays the filtered groups and strings based on the current filters.
        """
        print(
            'Search term: "',
            self.search_term,
            '", Filter type: "',
            self.filter_type,
            '", Mode: ',
            self.current_mode,
        )
        filtered_items = self.filter()
        result = {}
        for group, s, _ in filtered_items:
            if group not in result:
                result[group] = []
            result[group].append(s)
        for group, strings in result.items():
            print(group)
            for s in strings:
                print(f" - {s}")

        print("-----------")


# Example usage
test = [
    "Names::first",
    "Names::second",
    "Names::third",
    "Ages::fourth",
    "Ages::fifth",
    "Figures::second",
    "Figures::forth",
    "Figures::seventh",
]
measurements = [
    "non_constant",
    "zero",
    "non_constant",
    "zero",
    "non_constant",
    "zero",
    "non_constant",
    "non_constant",
]

filter_system = GroupStringFilter()
filter_system.add_entries(test, measurements, "::")

# Initial display
filter_system.display()

# Set mode and search term, then display
# filter_system.set_mode("Group")
filter_system.set_search_term("f")
filter_system.display()

# Set measurement filter to non-constant and display
filter_system.set_filter(MeasurementType.NON_CONSTANT)
filter_system.display()

# Change search term and display
filter_system.set_search_term("fi")
filter_system.display()

# Change measurement filter to zero and display
filter_system.set_filter(MeasurementType.ZERO)
filter_system.display()

# Change back to all and display
filter_system.set_filter(MeasurementType.ALL)
filter_system.display()

# Change to group mode and set search term to "fi"
filter_system.set_mode("Group")
filter_system.set_search_term("fi")
filter_system.display()


import customtkinter as ctk
from collections import defaultdict


class ScrollableFrameManager:
    """ """

    def __init__(
        self,
        root: ctk.CTkScrollableFrame,
        initial_groups=10,
        initial_buttons_per_group=10,
    ) -> None:
        self.root: ctk.CTkScrollableFrame = root
        self.label_widgets = {}
        self.button_widgets = defaultdict(list)

        self.create_initial_widget_pool(initial_groups, initial_buttons_per_group)

    def create_initial_widget_pool(self, initial_groups, initial_buttons_per_group):
        for i in range(initial_groups):
            label = ctk.CTkLabel(
                self.root,
                anchor="w",
                font=ctk.CTkFont(
                    family="Kento",
                    size=12,
                    weight="bold",
                ),
            )
            self.label_widgets[f"group_{i}"] = label

            for _ in range(initial_buttons_per_group):
                button = ctk.CTkButton(self.root)
                self.button_widgets[f"group_{i}"].append(button)

    def get_or_create_label(self, group_index):
        if f"group_{group_index}" in self.label_widgets:
            return self.label_widgets[f"group_{group_index}"]

        label = ctk.CTkLabel(
            self.root,
            anchor="w",
            font=ctk.CTkFont(
                family="Kento",
                size=12,
                weight="bold",
            ),
        )
        self.label_widgets[f"group_{group_index}"] = label

        return label

    def get_or_create_button(self, group_index, button_index):
        if button_index < len(self.button_widgets[f"group_{group_index}"]):
            return self.button_widgets[f"group_{group_index}"][button_index]

        button = ctk.CTkButton(
            self.root,
            height=25,
            corner_radius=7,
            font=ctk.CTkFont(
                family="Kento",
                size=12,
            ),
        )
        self.button_widgets[f"group_{group_index}"].append(button)

        return button

    def update_scrollable_frame(
        self, entries, seperator: str = "", sub_header_first: bool = True
    ):
        if seperator != "":
            parsed_entries = defaultdict(list)

            for entry in entries:
                if sub_header_first:
                    group_name, substring = entry.split(seperator)
                else:
                    substring, group_name = entry.split(seperator)

                group_name = group_name.strip()
                substring = substring.strip()

                parsed_entries[group_name].append(substring)

            for label in self.label_widgets.values():
                label.grid_forget()
            for buttons in self.button_widgets.values():
                for button in buttons:
                    button.grid_forget()

            current_row = 0
            for group, substrings in parsed_entries.items():
                label = self.get_or_create_label(current_row)
                label.configure(text=group.upper())
                label.grid(
                    row=current_row, column=0, sticky="nesw", padx=(7, 7), pady=(1, 1)
                )

                current_row += 1

                for i, substring in enumerate(substrings):
                    button = self.get_or_create_button(current_row - 1, i)
                    button.configure(text=substring)
                    button.grid(
                        row=current_row,
                        column=0,
                        sticky="nesw",
                        padx=(2, 2),
                        pady=(0, 3),
                    )

                    current_row += 1
        else:
            for label in self.label_widgets.values():
                label.grid_forget()

            for buttons in self.button_widgets.values():
                for button in buttons:
                    button.grid_forget()

            for i, entry in enumerate(entries):
                entry = entry.strip()

                button = self.get_or_create_button(0, i)
                button.configure(text=entry)
                button.grid(row=i, column=0, sticky="nesw", padx=(2, 2), pady=(0, 3))


if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("400x600")

    scrollable_frame = ctk.CTkScrollableFrame(app, width=200, height=450)
    scrollable_frame.columnconfigure(0, weight=1)
    scrollable_frame.pack(pady=20, padx=10)
    scrollable_frame_manager = ScrollableFrameManager(scrollable_frame)

    entries = [
        "Names::first",
        "Names::second",
        "Names::third",
        "Ages::fourth",
        "Ages::fifth",
        "Figures::second",
        "Figures::forth",
        "Figures::seventh",
    ]
    scrollable_frame_manager.update_scrollable_frame(entries)

    def on_update_button_click():
        new_entries = [
            "Colors::red",
            "Colors::blue",
            "Colors::green",
            "Shapes::circle",
            "Shapes::square",
            "Shapes::triangle",
        ]
        scrollable_frame_manager.update_scrollable_frame(new_entries, seperator="::")

    def on_update_sec_button_click():
        entries = [
            "Names::first",
            "Names::second",
            "Names::third",
            "Ages::fourth",
            "Ages::fifth",
            "Figures::second",
            "Figures::forth",
            "Figures::seventh",
        ]
        scrollable_frame_manager.update_scrollable_frame(entries)

    update_button = ctk.CTkButton(
        app, text="Update List", command=on_update_button_click
    )
    update_button.pack(pady=10)

    update_sec_button = ctk.CTkButton(
        app, text="Update List", command=on_update_sec_button_click
    )
    update_sec_button.pack(pady=10)

    app.mainloop()
