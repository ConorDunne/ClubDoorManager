class Member:
	memberId = None
	name = None
	membershipPaid = None
	attendance = None
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
			self.attendance = details["attended"]
		else:
			self.attendance = []

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
		if self.attendance:
			out["attended"] = self.attendance
		if self.comment != "":
			out["comment"] = self.comment
		
		return out
