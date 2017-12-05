import logging
import json
from actingweb import aw_web_request

class on_aw_base():

    def __init__(self):
        self.config = None
        self.myself = None
        self.webobj = None
        self.auth = None

    @classmethod
    def aw_init(self, auth, webobj=aw_web_request.aw_webobj()):
        self.auth = auth
        self.webobj = webobj
        self.config = auth.config
        self.myself = auth.actor

    @classmethod
    def bot_post(self, path):
        """Called on POSTs to /bot.

        Note, there will not be any actor initialised.
        """

        # Safety valve to make sure we don't do anything if bot is not
        # configured.
        if not self.config.bot['token'] or len(self.config.bot['token']) == 0:
            return False

        #try:
        #     body = json.loads(req.request.body.decode('utf-8', 'ignore'))
        #     logging.debug('Bot callback: ' + req.request.body.decode('utf-8', 'ignore'))
        #except:
        #     return 405
        #
        # This is how actor can be initialised if the bot request
        # contains a value that has been stored as an actor property.
        # This value must be a primary key for the external oauth identity
        # that the actor is representing.
        # Here, oauthId (from oauth service) has earlier been stored as a property
        #myself = actor.actor()
        #myself.get_from_property(name='oauthId', value=<PROPERTY-VALUE>)
        #if myself.id:
        #    logging.debug('Found actor(' + myself.id + ')')
        #
        # If we havent''
        #if not myself.id:
        #    myself.create(url=self.config.root, creator= <EMAIL>,
        #                    passphrase=self.config.newToken())
            #Now store the oauthId propery
        #    myself.setProperty('oauthId', <ID-VALUE>)
            # Send comfirmation message that actor has been created
        #    return True
        # Do something
        return True

    @classmethod
    def get_callbacks(self, name):
        """Customizible function to handle GET /callbacks"""
        # return True if callback has been processed
        # THE BELOW IS SAMPLE CODE
        #my_oauth=oauth.oauth(token = myself.getProperty('oauth_token').value)
        # if name == 'something':
        #    return
        # END OF SAMPLE CODE
        return False

    @classmethod
    def delete_callbacks(self, name):
        """Customizible function to handle DELETE /callbacks"""
        # return True if callback has been processed
        return False

    @classmethod
    def post_callbacks(self, name):
        """Customizible function to handle POST /callbacks"""
        # return True if callback has been processed
        # THE BELOW IS SAMPLE CODE
        #logging.debug("Callback body: "+req.request.body.decode('utf-8', 'ignore'))
        # non-json POSTs to be handled first
        # if name == 'somethingelse':
        #    return True
        # Handle json POSTs below
        #body = json.loads(req.request.body.decode('utf-8', 'ignore'))
        #data = body['data']
        # if name == 'somethingmore':
        #    callback_id = req.request.get('id')
        #    req.response.set_status(204)
        #    return True
        #req.response.set_status(403, "Callback not found.")
        # END OF SAMPLE CODE
        return False

    @classmethod
    def post_subscriptions(self, sub, peerid, data):
        """Customizible function to process incoming callbacks/subscriptions/ callback with json body, return True if processed, False if not."""
        logging.debug("Got callback and processed " + sub["subscriptionid"] +
                      " subscription from peer " + peerid + " with json blob: " + json.dumps(data))
        return True

    @classmethod
    def delete_actor(self):
        # THIS METHOD IS CALLED WHEN AN ACTOR IS REQUESTED TO BE DELETED.
        # THE BELOW IS SAMPLE CODE
        # Clean up anything associated with this actor before it is deleted.
        # END OF SAMPLE CODE
        return

    @classmethod
    def check_on_oauth_success(self, token=None):
        # THIS METHOD IS CALLED WHEN AN OAUTH AUTHORIZATION HAS BEEN SUCCESSFULLY MADE AND BEFORE APPROVAL
        return True

    @classmethod
    def actions_on_oauth_success(self):
        # THIS METHOD IS CALLED WHEN AN OAUTH AUTHORIZATION HAS BEEN SUCCESSFULLY MADE
        return True

    @classmethod
    def get_resources(self, name):
        """ Called on GET to resources. Return struct for json out.

            Returning {} will give a 404 response back to requestor.
        """
        return {}

    @classmethod
    def delete_resources(self, name):
        """ Called on DELETE to resources. Return struct for json out.

            Returning {} will give a 404 response back to requestor.
        """
        return {}

    @classmethod
    def put_resources(self, name, params):
        """ Called on PUT to resources. Return struct for json out.

            Returning {} will give a 404 response back to requestor.
            Returning an error code after setting the response will not change
            the error code.
        """
        return {}

    @classmethod
    def post_resources(self, name, params):
        """ Called on POST to resources. Return struct for json out.

            Returning {} will give a 404 response back to requestor.
            Returning an error code after setting the response will not change
            the error code.
        """
        return {}

    @classmethod
    def www_paths(self, path=''):
        # THIS METHOD IS CALLED WHEN AN actorid/www/* PATH IS CALLED (AND AFTER ACTINGWEB DEFAULT PATHS HAVE BEEN HANDLED)
        # THE BELOW IS SAMPLE CODE
        # if path == '' or not myself:
        #    logging.info('Got an on_www_paths without proper parameters.')
        #    return False
        # if path == 'something':
        #    return True
        # END OF SAMPLE CODE
        return False