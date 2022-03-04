class Member:
	memberId = None
	name = None
	membershipPaid = None
	attended = None
	card = None
	comment = None

	def __init__(self, memberId, details):
		self.memberId = memberId
		self.name = details["name"]
		self.membershipPaid = details["membershipPaid"]

		if "attended" in details:
			self.attended = details["attended"]
		else:
			self.attended = []

		if "card" in details:
			self.card = details["card"]
		else:
			self.card = []

		if "comment" in details:
			self.comment = details["comment"]
		else:
			self.comment = ""

	def toJson(self):
		out = {}
		
		out["name"] = self.name
		out["membershipPaid"] = self.membershipPaid

		if self.attended:
			out["attended"] = self.attended
		if self.card:
			out["card"] = self.card
		if self.comment != "":
			out["comment"] = self.comment
		
		return out
