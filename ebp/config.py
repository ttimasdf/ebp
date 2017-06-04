import configparser

BACKUP_SUFFIX = ".bak"

_parser = configparser.ConfigParser()


def parse_file(filename):
    """Return all infomation you needed to patch files"""
    _parser.read(filename)
    result = {'files': {}}
    result['metadata'] = {
        "name": _parser['metadata']['name'],
        "description": _parser['metadata']['description'],
        "congratulation": _parser['metadata']['congratulation'],
    } if 'metadata' in _parser else {}

    for patch_name in _parser.sections():
        if not patch_name.startswith('patch:'):
            continue
        s = _parser[patch_name]
        patch_name = patch_name[6:]
        this = {
            "unsign": s.getboolean('unsign', False),
            "file": s['file'],
            "relatives": [],
            "absolutes": [],
        }

        if 'relatives' in s:
            for line in s['relatives'].strip('\n, ').split('\n'):
                line = line.split(',')
                this['relatives'].append({
                    "src": bytes.fromhex(line[0]),
                    "dst": bytes.fromhex(line[1]),
                    "fg": zip(
                        (int(i) for i in line[2::2]),
                        (bytes.fromhex(i) for i in line[3::2])),
                })
        if 'absolutes' in s:
            for line in s['absolutes'].strip('\n, ').split('\n'):
                this['absolutes'].append({
                    "pos": int(line[0]),
                    "src": bytes.fromhex(line[1]),
                    "dst": bytes.fromhex(line[2]),
                })

        result['files'][patch_name] = this

    return result
