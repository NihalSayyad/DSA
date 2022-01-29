from Implemantation import TreeNode


class MyTreeNode(TreeNode):
    def __init__(self, name, designation):
        self.name = name
        super().__init__(designation)

    def print_tree(self, property_name):
        if property_name == "name":
            value = self.name
        elif property_name == "both":
            value = self.name + " ( " + self.data + " )"
        elif property_name == "designation":
            value = self.data
            
            
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|--"
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)


def build_product_tree():
    # CTO Hierarchy
    infra_head = MyTreeNode("Vishwa", "Infrastructure Head")
    infra_head.add_child(MyTreeNode("Dhaval", "Cloud Manager"))
    infra_head.add_child(MyTreeNode("Abhijit", "App Manager"))

    cto = MyTreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(MyTreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = MyTreeNode("Gels", "HR Head")

    hr_head.add_child(MyTreeNode("Peter", "Recruitment Manager"))
    hr_head.add_child(MyTreeNode("Waqas", "Policy Manager"))

    ceo = MyTreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree("both")

    print("---------------------------------------")
    root.print_tree("name")

    print("---------------------------------------")
    root.print_tree("designation")
