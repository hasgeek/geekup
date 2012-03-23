from datetime import datetime
from flask import g
from coaster.docflow import DocumentWorkflow, WorkflowState, WorkflowStateGroup
from geekup.models import Event, EventStatus
from geekup.views.login import lastuser


class EventWorkflow(DocumentWorkflow):
	"""
    Workflow for Geekup events.
    """

    state_attr = 'status'

    draft = WorkflowState(EventStatus.DRAFT, title=u"Draft")
    active = WorkflowState(EventStatus.ACTIVE, title=u"Active")
    closed = WorkflowState(EventStatus.CLOSED, title=u"Closed")
    completed = WorkflowState(EventStatus.COMPLETED, title=u"Completed")
    cancelled = WorkflowState(EventStatus.CANCELLED, title=u"Cancelled")
    rejected = WorkflowState(EventStatus.REJECTED, title=u"Rejected")
    withdrawn = WorkflowState(EventStatus.WITHDRAWN, title=u"Withdrawn")

     #: States in which an owner can edit
    editable = WorkflowStateGroup([draft, active], title=u"Editable")
    #: States in which a reviewer can view
    reviewable = WorkflowStateGroup([draft, active, closed, rejected, completed],
                                    title=u"Reviewable")


    def permissions(self):
        """
        Permissions available to current user.
        """
        base_permissions = super(EventWorkflow,
                                 self).permissions()
        if self.document.user == g.user:
            base_permissions.append('owner')
        base_permissions.extend(lastuser.permissions())
        return base_permissions

    @draft.transition(active, 'owner', title=u"Open", category="primary",
        description=u"Open the Geekup for registrations.", view="event_open")
    def open(self):
        """
        Open the Geekup.
        """
        # Update timestamp
        self.document.datetime = datetime.utcnow()
	
	@draft.transition(cancelled, 'owner', title=u"Cancel", category="warning",
		description=u"Cancel the Geekup, before opening.", view="event_cancel" )
	def cancel(self):
		"""
		Cancel the Geekup
		"""
		pass

	@draft.transition(rejected, 'owner', title=u"Rejected", category="danger"
		description=u"Reject the Geekup proposed by someone else", view="event_reject")
	def reject(self):
		"""
		Reject the Geekup
		"""
		pass

	@draft.transition(withdrawn, 'owner', title=u"Withdraw", category="danger"
        description=u"Withdraw the Geekup",view="event_withdraw")
    def withdraw(self):
        """
        Withdraw the Geekup
        """
        pass

	@active.transition(closed, 'owner', title=u"Close", category="primary"
        description=u"Close registrations for the Geekup",view="event_close")
    def close(self):
        """
        Close the Geekup
        """
        pass


	@close.transition(completed, 'owner',title=u"Complete", category="success"
        description=u"Geekup completed",view="event_completed")
    def complete(self):
        """
        Geekup is now completed.
        """
        pass

Even.apply_on(Event)
