#!/usr/bin/env python
# encoding: utf-8


from ansible.plugins.callback.default import CallbackModule as CallbackModule_default


DOCUMENTATION = '''
    callback: cleanoutput
    type: stdout
    short_description: prints stdout and stderr without indentation
    description:
        - This callback prints stdout and stderr as produced by shell or command
          modules.
    requirements:
        - ansible
        - whitelist in ansible.cfg
        - set as stdout_callback ansible.cfg
'''


class CallbackModule(CallbackModule_default):  # pylint: disable=too-few-public-methods,no-init
    '''
    Override for the default callback module.
    Render std err/out outside of the rest of the result which it prints with
    indentation.
    '''
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'cleanoutput'

    def _dump_results(self, result):
        '''Return the text to output for a result.'''

        # Enable JSON identation
        result['_ansible_verbose_always'] = True

        save = {}
        for key in ['stdout', 'stdout_lines', 'stderr', 'stderr_lines', 'msg']:
            if key in result:
                save[key] = result.pop(key)

        output = CallbackModule_default._dump_results(self, result)

        for key in ['stdout', 'stderr', 'msg']:
            if key in save and save[key]:
                output += '\n%s:\n%s\n' % (key.upper(), save[key])

        for key, value in save.items():
            result[key] = value

        return output
