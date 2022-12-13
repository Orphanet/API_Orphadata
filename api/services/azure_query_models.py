import base64
import hmac
from urllib.request import Request



class queryParams:
    def __init__(self, request: Request) -> None:
        self.operation = request.args.get('operation', 'SignUp')
        self.salt = request.args.get('salt', 'Undefined salt')
        self.sig = request.args.get('sig', 'Undefined sig')

        self.errorMessage = request.args.get('errorMessage', None)        
        
        if self.operation in ['SignIn',  'SignUp', 'SignOut']:
            self.returnUrl = request.args.get('returnUrl', 'Undefined returnUrl')

        elif self.operation in ['Subscribe', 'Unsubscribe', 'Renew']:
            self.productId = request.args.get('productId', 'Undefined productId')
            self.subscriptionId = request.args.get('subscriptionId', 'Undefined subscriptionId')
            self.userId = request.args.get('userId', 'Undefined userId')

        elif self.operation in ['ChangePassword', 'ChangeProfile', 'CloseAccount']:
            self.userId = request.args.get('userId', 'Undefined userId')


    def validate_request(self) -> bool:
        """Check if request comes from Azure API management service.

        How it works: query parameters are used to create a chain message.
        This chain message is hashed (somehow transformed) through a secret key
        shared between Azure (the resource provider) and an Azure resource user (you).
        When a request is done, a signature is sent with query parameters.
        This signature is the result of the chain message hashed through the secret key.
        
        After receiving the request, if the hashed chain message match the signature,
        it means that signature has been sent by someone that knows the secret key: Azure.

        Parameters
        ----------
        _type : string
            Either 'signInsignUp', 'subscribe' or 'unsubscribe'

        Returns
        -------
        bool
            True if the hashed chain message matches the expected signature, False otherwise.
        """
        # secret_key = os.getenv('APIM_DELEGATION_KEY', 'aW50ZWdyYXRpb24mMjAyMjEwMjkxNDE2JlJNc3ZGODVDMGppRTFRRFhoNjM5bzhGRmszdjFSbFEvdDNCcVpwQUJDNGd6ZGFvYTVPY2RTclFOM2IzSlhNUzFBSlRacnd0R3RzY1VXUnJBU3p2SXVBPT0=')
        secret_key = 'aW50ZWdyYXRpb24mMjAyMjEwMjkxNDE2JlJNc3ZGODVDMGppRTFRRFhoNjM5bzhGRmszdjFSbFEvdDNCcVpwQUJDNGd6ZGFvYTVPY2RTclFOM2IzSlhNUzFBSlRacnd0R3RzY1VXUnJBU3p2SXVBPT0='

        if self.operation in ['SignIn','SignUp', 'SignOut']:
            query_params = [self.salt, self.returnUrl]
        elif self.operation == 'Subscribe':
            query_params = [self.salt, self.productId, self.userId]
        elif self.operation == 'Unsubscribe':
            query_params = [self.salt, self.subscriptionId]

        message = bytes('\n'.join(query_params), 'utf-8')
        encoder = hmac.new(bytes(base64.b64decode(secret_key).decode('utf-8'), 'utf-8'), digestmod='sha512')
        encoder.update(message)

        calculated_signature = base64.b64encode(encoder.digest()).decode()
        expected_signature = self.sig.encode("utf-8").decode()

        return hmac.compare_digest(calculated_signature, expected_signature)
