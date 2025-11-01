class ProgrammingLanguage:
    def __init__(self, id, name, year):
        self.id = id
        self.name = name
        self.year = year


class DevelopmentTool:
    def __init__(self, id, name, license_cost, lang_id):
        self.id = id
        self.name = name
        self.license_cost = license_cost
        self.lang_id = lang_id


class LangTool:
    def __init__(self, lang_id, tool_id):
        self.lang_id = lang_id
        self.tool_id = tool_id

languages = [
    ProgrammingLanguage(1, 'Python', 1991),
    ProgrammingLanguage(2, 'Java', 1995),
    ProgrammingLanguage(3, 'C++', 1985),
    ProgrammingLanguage(4, 'JavaScript', 1995),
    ProgrammingLanguage(5, 'Go', 2009),
]

tools = [
    DevelopmentTool(1, 'PyCharm', 199, 1),
    DevelopmentTool(2, 'IntelliJ IDEA', 249, 2),
    DevelopmentTool(3, 'Visual Studio', 299, 3),
    DevelopmentTool(4, 'WebStorm', 199, 4),
    DevelopmentTool(5, 'GoLand', 199, 5),
    DevelopmentTool(6, 'VS Code', 0, 1),
    DevelopmentTool(7, 'Eclipse', 0, 2),
]

langs_tools = [
    LangTool(1, 1),
    LangTool(1, 6),
    LangTool(2, 2),
    LangTool(2, 7),
    LangTool(3, 3),
    LangTool(4, 4),
    LangTool(5, 5),
    LangTool(1, 3),
    LangTool(2, 4),
]


def main():
    one_to_many = [(tool.name, tool.license_cost, lang.name)
                   for lang in languages
                   for tool in tools
                   if tool.lang_id == lang.id]

    many_to_many_temp = [(lang.name, lt.lang_id, lt.tool_id)
                         for lang in languages
                         for lt in langs_tools
                         if lang.id == lt.lang_id]

    many_to_many = [(tool.name, tool.license_cost, lang_name)
                    for lang_name, lang_id, tool_id in many_to_many_temp
                    for tool in tools if tool.id == tool_id]

    print('Задание 1')
    res_g1 = [(tool_name, lang_name)
              for tool_name, _, lang_name in one_to_many
              if tool_name.startswith('V')]
    print("Средства разработки, начинающиеся на 'V':")
    print(res_g1 if res_g1 else "Не найдено")

    print('\nЗадание 2')
    lang_tools_dict = {}
    for tool_name, license_cost, lang_name in one_to_many:
        if lang_name not in lang_tools_dict:
            lang_tools_dict[lang_name] = []
        lang_tools_dict[lang_name].append((tool_name, license_cost))

    res_g2_unsorted = []
    for lang_name, tool_list in lang_tools_dict.items():
        max_tool = max(tool_list, key=lambda x: x[1])
        res_g2_unsorted.append((lang_name, max_tool[0], max_tool[1]))

    res_g2 = sorted(res_g2_unsorted, key=lambda x: x[2], reverse=True)
    print("Языки с максимальной стоимостью лицензии средств разработки:")
    for lang, tool, cost in res_g2:
        print(f"{lang}: {tool} - ${cost}")

    print('\nЗадание 3')
    res_g3 = sorted(many_to_many, key=lambda x: (x[2], x[0]))
    print("Все связанные средства разработки и языки программирования:")
    for tool, cost, lang in res_g3:
        print(f"{lang}: {tool} - ${cost}")


if __name__ == '__main__':
    main()