

class CheckAPI:

    @classmethod
    def check_single_page_url(cls, part_url, line, num_after=0):
        part_line = line.split(part_url, 1)
        if len(part_line) == 2 and part_line[1][:num_after].isdigit():
            return True
        return False

    @classmethod
    def check_general_page_url(cls, part_url, line, params_after=''):
        part_line = line.split(part_url, 1)
        if len(part_line) == 2 and params_after == '' and part_line[1][0] == ';':
            return True
        if len(part_line) == 2 and params_after != '' and part_line[1][0] == '?':
            params_part_line = part_line[1].split(';', 1)
            if isinstance(params_after, list):
                for p in params_after:
                    if p not in params_part_line[0]:
                        return False
                return True
            elif params_after in params_part_line[0]:
                return True
        return False