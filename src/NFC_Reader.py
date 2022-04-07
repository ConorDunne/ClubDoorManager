from smartcard.scard import *
from smartcard.util import toHexString
import smartcard.util
from smartcard.ATR import ATR
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnectionObserver import CardConnectionObserver
import time
import struct
import array

GET_UID = [0xFF,0xCA,0x00,0x00,0x04]

class NFC_Reader():
	def __init__(self, uid = ""):
		self.uid = uid
		self.hresult, self.hcontext = SCardEstablishContext(SCARD_SCOPE_USER)
		self.hresult, self.readers = SCardListReaders(self.hcontext, [])
		assert len(self.readers) > 0
		self.reader = self.readers[0]
		
	def CardPresent(self):
		self.hresult, self.hcard, self.dwActiveProtocol = SCardConnect(
				self.hcontext,
				self.reader,
				SCARD_SHARE_SHARED,
				SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1)
		self.data_blocks = []

		return (self.hresult == 0)

	def GetUID(self):
		self.response = None
		value = None
		for iteration in range(1):
			try:
				self.hresult, self.response = SCardTransmit(self.hcard,self.dwActiveProtocol,GET_UID)
				value = toHexString(self.response, format=0)
			except SystemError:
				print ("No Card Found")
		return value



def ReadCard():
	r = NFC_Reader()

	if not r.CardPresent():
		return -1;

	return r.GetUID()



if __name__ == "__main__":
	print(ReadCard())
			