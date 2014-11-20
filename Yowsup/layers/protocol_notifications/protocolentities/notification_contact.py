from Yowsup.structs import ProtocolEntity, ProtocolTreeNode
from .notification import NotificationProtocolEntity
class ContactNotificationProtocolEntity(NotificationProtocolEntity):
    '''
    <notification offline="0" id="{{NOTIFICATION_ID}}" notify="{{NOTIFY_NAME}}" type="contacts" 
            t="{{TIMESTAMP}}" from="{{SENDER_JID}}">
        <remove jid="{{contact_jid}}"></remove>
    </notification>
    
    '''

    def __init__(self, _type, _id,  _from, status, timestamp, notify, offline = False):
        super(ContactNotificationProtocolEntity, self).__init__("contacts", _id, _from, timestamp, notify, offline)


    @staticmethod
    def fromProtocolTreeNode(node):
        entity = NotificationProtocolEntity.fromProtocolTreeNode(node)
        entity.__class__ = ContactNotificationProtocolEntity
        return entity