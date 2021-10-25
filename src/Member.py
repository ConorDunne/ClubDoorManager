class Member:
	memberId = None
	name = None
	membershipPaid = None
	attended = None
	balance = None
	comment = None

	def __init__(self, memberId, details):
		self.memberId = memberId
		self.name = details["name"]
		self.membershipPaid = details["membershipPaid"]

		if "balance" in details:
			self.balance = details["balance"]
		else:
			self.balance = 0.0

		if "attended" in details:
			self.attended = details["attended"]
		else:
			self.attended = []

		if "comment" in details:
			self.comment = details["comment"]
		else:
			self.comment = ""

	def toJson(self):
		out = {}
		
		out["name"] = self.name
		out["membershipPaid"] = self.membershipPaid

		if self.balance != 0.0:
			out["balance"] = self.balance
		if self.attended:
			out["attended"] = self.attended
		if self.comment != "":
			out["comment"] = self.comment
		
		return out
