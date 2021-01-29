class Version:
    def __init__(self, version):
        self.version = version


    def appened_additional_symbols(self, version_list):
        while len(version_list) < 4:
            version_list.append('0')
        return version_list

    def __lt__(self, other):
        self_version = self.version.replace('-', '.').split('.')
        self_version = self.appened_additional_symbols(self_version)
        other_version = other.version.replace('-', '.').split('.')
        other_version = self.appened_additional_symbols(other_version)
        list_versions = [(self_version[iter_], other_version[iter_]) for iter_ in range(4)]
        for version_1, version_2 in list_versions:
            if version_1.isdigit() and version_2.isdigit():
                if int(version_1) < int(version_2):
                    return True
                else:
                    continue
            else:
                if version_1 == 'alpha' and (version_2 != 'alpha' or version_2.isdigit()):
                    return True
                elif version_2 == 'alpha' and (version_1 != 'alpha' or version_1.isdigit()):
                    return False
                elif version_1[-1] == 'b' and (version_2[-1] != 'b' or version_2.isdigit()):
                    return True
                elif version_2[-1] == 'b' and (version_1[-1] != 'b' or version_1.isdigit()):
                    return False
                elif version_1 == 'rc' and (version_2 != 'rc' or version_2.isdigit()):
                    return True
                elif version_2 == 'rc' and (version_1 != 'rc' or version_1.isdigit()):
                    return False
                else:
                    return True


    def __eq__(self, other):
        self_version = self.version.replace('-', '.').split('.')
        self_version = self.appened_additional_symbols(self_version)
        other_version = other.version.replace('-', '.').split('.')
        other_version = self.appened_additional_symbols(other_version)
        list_versions = [(self_version[iter_], other_version[iter_]) for iter_ in range(4)]
        for version_1, version_2 in list_versions:
            if version_1 == version_2:
                continue
            else:
                return False
        return True












def main():
    to_test = [
        ('1.0.alpha', '1.0.0.alpha'),
        # ('1.0.0', '1.42.0'),
        # ('1.2.0', '1.2.42'),
        # ('1.1.0-alpha', '1.2.0-alpha.1'),
        # ('1.0.1b', '1.0.10-alpha.beta'),
        # ('1.0.0-rc.1', '1.0.0'),
    ]

    for version_1, version_2 in to_test:
        # assert Version(version_1) < Version(version_2), 'le failed'
        # assert Version(version_2) > Version(version_1), 'ge failed'
        print(Version(version_2) == Version(version_1))
        assert Version(version_2) == Version(version_1), 'neq failed'


if __name__ == "__main__":
    main()
    # print(Version('1.0.0') < Version('2.0.0'))