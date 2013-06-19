from twisted.protocols import amp

class GetInfo(amp.Command):
    arguments = []
    response = [
        ('commands', amp.AmpList([
            ('name', amp.String()),
            ('version', amp.Integer()),
            ])
        ),
        ('environ', amp.AmpList([
            ('key', amp.String()),
            ('value', amp.String()),
            ])
        ),
        ('system', amp.String()),
        ('basedir', amp.String()),
        ('version', amp.String()),
    ]


class SetBuilderList(amp.Command):
    """
    Given a list of builders and their build directories, ensures that those
    builders, and only those builders, are running.
    This can be called after the initial connection is established, with a new
    list, to add or remove builders.
    """
    arguments = [ ('builders', 
        amp.AmpList([
            ('name', amp.String()),
            ('dir', amp.String()),
        ]))
    ]
    response = [('result', amp.Integer())] #  0 for success, 1 or others are error codes
