import base64
import hmac
from urllib.request import Request
import os

class queryParams:
    def __init__(self, request: Request) -> None:
        self.operation = request.args.get('operation', 'SignUp')
        self.errorMessage = request.args.get('errorMessage', None)        
        
        if self.operation in ['SignIn',  'SignOut']:
            self.returnUrl = request.args.get('returnUrl', None)
            self.salt = request.args.get('salt', None)
            self.sig = request.args.get('sig', None)

        elif self.operation in ['Subscribe', 'Unsubscribe', 'Renew']:
            self.productId = request.args.get('productId', None)
            self.subscriptionId = request.args.get('subscriptionId', None)
            self.userId = request.args.get('userId', None)
            self.salt = request.args.get('salt', None)
            self.sig = request.args.get('sig', None)

        elif self.operation in ['ChangePassword', 'ChangeProfile', 'CloseAccount']:
            self.userId = request.args.get('userId', None)
            self.salt = request.args.get('salt', None)
            self.sig = request.args.get('sig', None)


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
        try:
            if self.operation in ['SignIn','SignUp', 'SignOut']:
                query_params = [self.salt, self.returnUrl]
            if self.operation == 'Subscribe':
                query_params = [self.salt, self.productId, self.userId]
            if self.operation == 'Unsubscribe':
                query_params = [self.salt, self.subscriptionId]
        except:
            return False

        message = bytes('\n'.join(query_params), 'utf-8')

        secret_key = os.getenv('APIM_DELEGATION_KEY')
        if not secret_key:
              return False

        encoder = hmac.new(bytes(base64.b64decode(bytes(secret_key, "utf-8")).decode('utf-8'), 'utf-8'), digestmod='sha512')
        encoder.update(message)

        return hmac.compare_digest(base64.b64encode(encoder.digest()).decode(), self.sig)
