
from fasthtml.common import *
from fasthtml.svg import *

# Set up the app
tlink = Script(src="https://cdn.tailwindcss.com"),
app = FastHTML(hdrs=(tlink, ), pico=False)

#js
accordian_script = Script("""
document.querySelectorAll('.accordion-trigger').forEach(button => {
    button.addEventListener('click', () => {
        const accordionItem = button.closest('.accordion-item');
        const wasOpen = accordionItem.dataset.state === 'open';

        // Close all accordion items
        document.querySelectorAll('.accordion-item').forEach(item => {
            item.dataset.state = 'closed';
            item.querySelector('.accordion-content').hidden = true;
            item.querySelector('.accordion-trigger').dataset.state = 'closed';
            item.querySelector('.accordion-trigger svg').style.transform = 'rotate(0deg)';
        });

        // If the clicked item wasn't open before, open it
        if (!wasOpen) {
            accordionItem.dataset.state = 'open';
            accordionItem.querySelector('.accordion-content').hidden = false;
            button.dataset.state = 'open';
            button.querySelector('svg').style.transform = 'rotate(180deg)';
        }
    });
});
""")

def FAQI(q, a, buy_btn=False):
    return Div(
            H3(
                Button(
                    P(q, cls="mx-3"),
                    Svg(
                        Path(d='m6 9 6 6 6-6'),
                        xmlns='http://www.w3.org/2000/svg',
                        width='24',
                        height='24',
                        viewbox='0 0 24 24',
                        fill='none',
                        stroke='currentColor',
                        stroke_width='2',
                        stroke_linecap='round',
                        stroke_linejoin='round',
                        cls='mx-3 lucide lucide-chevron-down h-4 w-4 shrink-0 transition-transform duration-200'
                    ),
                    type='button',
                    aria_controls='radix-:r1:',
                    aria_expanded='true',
                    data_state='closed',
                    data_orientation='vertical',
                    id='radix-:r0:',
                    data_id='72',
                    data_radix_collection_item='',
                    cls='accordion-trigger flex flex-1 items-center justify-between py-4 transition-all hover:underline [&[data-state=open]>svg]:rotate-180 bg-[#e67e22] text-[#2c3e50] font-bold'
                ),
                data_orientation='vertical',
                data_state='closed',
                cls='flex'
            ),
            Div(
                Div(
                    P(a, data_id='74', cls='m-3 text-[#555]'),
                    A('Buy Now', href='/buy-now', cls='mx-3 inline-flex h-9 items-center justify-center rounded-md bg-[#e74c3c] px-4 py-2 text-sm font-medium text-primary-foreground shadow transition-colors hover:bg-[#c0392b] focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50') if buy_btn else "",
                    cls='pb-4 pt-0'
                ),
                data_state='closed',
                id='radix-:r1:',
                role='region',
                aria_labelledby='radix-:r0:',
                data_orientation='vertical',
                data_id='73',
                hidden='',
                style='--radix-accordion-content-height: var(--radix-collapsible-content-height); --radix-accordion-content-width: var(--radix-collapsible-content-width); --radix-collapsible-content-height: 79.98949432373047px; --radix-collapsible-content-width: 487.9989318847656px;',
                cls='accordion-content overflow-hidden text-sm transition-all data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down'
            ),
            data_state='closed',
            data_orientation='vertical',
            data_id='71',
            cls='accordion-item border-b'
        )

page = Div(
    Header(
        A(
            Svg(
                Path(d='M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z'),
                Line(x1='4', x2='4', y1='22', y2='15'),
                xmlns='http://www.w3.org/2000/svg',
                width='24',
                height='24',
                viewbox='0 0 24 24',
                fill='none',
                stroke='currentColor',
                stroke_width='2',
                stroke_linecap='round',
                stroke_linejoin='round',
                cls='h-8 w-8'
            ),
            Span('NotFriend', cls='sr-only'),
            href='#',
            cls='flex items-center justify-center'
        ),
        Nav(
            A('Features', href='#', cls='text-sm font-medium hover:underline underline-offset-4'),
            A('Testimonials', href='#', cls='text-sm font-medium hover:underline underline-offset-4'),
            A('FAQ', href='#', cls='text-sm font-medium hover:underline underline-offset-4'),
            cls='ml-auto flex gap-4 sm:gap-6'
        ),
        cls='px-4 lg:px-6 h-14 flex items-center justify-between'
    ),
    Main(
        Section(
            Div(
                Div(
                    Div(
                        Div(
                            H1(
                                "The World's First",
                                Span('Non-Smart', cls='text-[#e74c3c]'),
                                'AI Pendant',
                                cls='lg:leading-tighter text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl xl:text-[3.4rem] 2xl:text-[3.75rem] text-[#2c3e50]'
                            ),
                            P('Introducing the NotFriend - the ultimate in anti-technology fashion. This literal plastic circle does\r\n              absolutely nothing, but looks great doing it.', cls='mx-auto max-w-[700px] text-[#555] md:text-xl'),
                            Div(
                                A('Buy Now', href='/buy-now', cls='inline-flex h-9 items-center justify-center rounded-md bg-[#e74c3c] px-4 py-2 text-sm font-medium text-primary-foreground shadow transition-colors hover:bg-[#c0392b] focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50'),
                                cls='space-x-4 mt-6'
                            ),
                            cls='my-auto space-y-6'

                        ),
                        
                        cls='flex flex-col items-center justify-center space-y-6'
                    ),
                    Div(
                        Img(src='/product_shot.jpeg', width='400', height='400', alt='NotFriend', cls='mx-auto aspect-square overflow-hidden rounded-full object-contain'),
                        cls='flex justify-center'
                    ),
                    cls='grid max-w-[1300px] mx-auto gap-4 px-4 sm:px-6 md:px-10 md:grid-cols-2 md:gap-16'
                ),
                cls='px-4 md:px-6 space-y-10 xl:space-y-16'
            ),
            cls='w-full py-6 md:py-12 lg:py-18 border-y'
        ),
        Section(
            Div(
                Div(
                    Div(
                        H2('Advanced Features', cls='text-3xl font-bold tracking-tighter sm:text-5xl text-[#2c3e50]'),
                        P('The NotFriend is packed with cutting-edge non-technology that will revolutionize your life in\r\n              absolutely no way.', cls='max-w-[900px] text-[#555] md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed'),
                        cls='space-y-2'
                    ),
                    cls='flex flex-col items-center justify-center space-y-4 text-center'
                ),
                Div(
                    Div(
                        H3('Literally Does Nothing', cls='text-lg font-bold text-[#2c3e50]'),
                        P("The NotFriend is a true marvel of non-engineering. It sits there. That's it.", cls='text-[#555]'),
                        cls='grid gap-1'
                    ),
                    Div(
                        H3('Unparalleled Simplicity', cls='text-lg font-bold text-[#2c3e50]'),
                        P('No buttons, no screens, no batteries. Just a beautiful, useless circle.', cls='text-[#555]'),
                        cls='grid gap-1'
                    ),
                    Div(
                        H3('Timeless Design', cls='text-lg font-bold text-[#2c3e50]'),
                        P('Crafted from the finest plastic, the NotFriend will never go out of style.', cls='text-[#555]'),
                        cls='grid gap-1'
                    ),
                    Div(
                        H3('Guaranteed Conversation Starter', cls='text-lg font-bold text-[#2c3e50]'),
                        P('Wear the NotFriend and watch as people ask, "What is that thing?"', cls='text-[#555]'),
                        cls='grid gap-1'
                    ),
                    Div(
                        H3('Eco-Friendly', cls='text-lg font-bold text-[#2c3e50]'),
                        P('The NotFriend has a zero carbon footprint, because it literally does nothing.', cls='text-[#555]'),
                        cls='grid gap-1'
                    ),
                    Div(
                        H3('Lifetime Warranty', cls='text-lg font-bold text-[#2c3e50]'),
                        P("Your NotFriend will last forever, because it's just a circle of plastic.", cls='text-[#555]'),
                        cls='grid gap-1'
                    ),
                    cls='mx-auto grid items-start gap-8 sm:max-w-4xl sm:grid-cols-2 md:gap-12 lg:max-w-5xl lg:grid-cols-3'
                ),
                cls='container space-y-12 px-4 md:px-6 mx-auto'
            ),
            cls='w-full py-12 md:py-24 lg:py-32 bg-[#f1c40f]'
        ),
        Section(
            Div(
                Div(
                    H2('What Our Customers Are Saying', cls='text-3xl font-bold tracking-tighter md:text-4xl/tight text-[#2c3e50]'),
                    P('Hear from the people who have experienced the life-changing power of the NotFriend.', cls='mx-auto max-w-[600px] text-[#555] md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed'),
                    cls='space-y-3'
                ),
                Div(
                    Div(
                        Div(
                            Div(
                                Div('"It\'s the best non-product I\'ve ever owned!"', cls='text-xl font-bold text-[#2c3e50]'),
                                Div('- Jane Doe, Imaginary NotFriend Enthusiast', cls='text-sm text-[#555]'),
                                cls='grid gap-2 text-left'
                            ),
                            cls='mx-auto flex w-full items-center justify-center p-4 sm:p-8'
                        ),
                        Div(
                            Div(
                                Div('"I can\'t imagine my life without my NotFriend."', cls='text-xl font-bold text-[#2c3e50]'),
                                Div('- John Smith, Imaginary NotFriend Addict', cls='text-sm text-[#555]'),
                                cls='grid gap-2 text-left'
                            ),
                            cls='mx-auto flex w-full items-center justify-center p-4 sm:p-8'
                        ),
                        cls='grid w-full grid-cols-1 items-stretch justify-center md:grid-cols-2'
                    ),
                    cls='divide-y rounded-lg border border-[#2c3e50]'
                ),
                cls='container grid items-center justify-center gap-4 px-4 text-center md:px-6 mx-auto'
            ),
            cls='w-full py-12 md:py-24 lg:py-32 bg-[#e67e22]'
        ),
        Section(
            Div(
                Div(
                    Div(
                        H2('Frequently Asked Questions', cls='text-3xl font-bold tracking-tighter sm:text-5xl text-[#2c3e50]'),
                        P("Still have questions about the NotFriend? We've got answers.", cls='max-w-[900px] text-[#555] md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed'),
                        cls='space-y-2'
                    ),
                    cls='flex flex-col items-center justify-center space-y-4 text-center'
                ),
                Div(
                    Div(
                        Div(
                            FAQI('What is the NotFriend?', "The NotFriend is a revolutionary non-smart pendant that does absolutely nothing. It's a literal circle of plastic that you can wear around your neck to make a bold statement about the absurdity of technology."),
                            FAQI('How does the NotFriend work?', 'The NotFriend doesn\'t work. It\'s a non-working, non-smart, non-technological device. You simply wear it and enjoy the fact that it does absolutely nothing.'),
                            FAQI('Why would I want a NotFriend?', 'The NotFriend is the perfect accessory for anyone who wants to make a statement about the over-saturation of technology in our lives. It\'s a bold, ironic, and humorous way to embrace the beauty of simplicity and non-functionality.'),
                            FAQI("Can I actually buy this?", "Yes, you can! The NotFriend is available for purchase on our website. Click the \"Buy Now\" button to get your very own non-smart AI pendant.", buy_btn=True),
                            data_orientation='vertical',
                            cls='border-[#2c3e50] rounded-lg'
                        ),
                        cls='flex flex-col justify-center space-y-4'
                    ),
                    Div(
                        Img(src='/product_shot.jpeg', width='400', height='400', alt='NotFriend', cls='mx-auto aspect-square overflow-hidden rounded-full object-contain'),
                        cls='flex justify-center'
                    ),
                    cls='mx-auto grid max-w-5xl items-center gap-6 py-12 lg:grid-cols-2 lg:gap-12'
                ),
                cls='container px-4 md:px-6 mx-auto'
            ),
            cls='w-full py-12 md:py-24 lg:py-32 bg-[#f1c40f]'
        ),
        cls='flex-1'
    ),
    Footer(
        P('© 2024 NotFriend Inc. All rights reserved.', cls='text-xs text-[#555]'),
        Nav(
            A(href='#', cls='text-xs hover:underline underline-offset-4 text-[#555]'),
            cls='sm:ml-auto flex gap-4 sm:gap-6'
        ),
        cls='flex flex-col gap-2 sm:flex-row py-6 w-full shrink-0 items-center px-4 md:px-6 border-t'
    ),
    cls='flex flex-col min-h-[100dvh] bg-gradient-to-b from-[#f1c40f] to-[#e67e22] text-[#333]'
)

@app.get('/')
def home():
    return Title("NotFriend"), page, accordian_script

@app.get('/buy-now')
def buy_now():
    form = Form(
        Select(
            Option('Physical', value='physical'),
            Option('Virtual', value='virtual'),
            required=True,
            name='product', id='product',
            cls='w-full px-4 py-2 border border-[#2c3e50] rounded-md mb-4'
        ),
        Input(type='email', placeholder='Email', required=True, name='email', id='email',
              cls='w-full px-4 py-2 border border-[#2c3e50] rounded-md mb-4'),
        Textarea(type='text', placeholder='Address', name='address', id='address',
              cls='w-full px-4 py-2 border border-[#2c3e50] rounded-md mb-4'),
        Button('Buy Now', type='submit', cls='w-full px-4 py-2 bg-[#e74c3c] text-white rounded-md'),
        action="/buy"
    )
    form = Div(
        H2('Buy Now ($24.96)', cls='pt-8 text-3xl font-bold tracking-tighter sm:text-5xl text-[#2c3e50]'),
        P('Please enter your email (required) and physical address (physical NotFriends only) to facilitate NotFriend delivery.', 
        cls='my-5  max-w-[900px] text-[#555] md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed'),
        form, 
        cls='max-w-[400px] mx-auto')
    return Title("Buy Now"), Body(form)

# For images, CSS, etc.
@app.get("/{fname:path}.{ext:static}")
def static(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')

# Stripe Stuff
import stripe
stripe.api_key = os.environ["STRIPE_KEY"]
webhook_secret = os.environ['STRIPE_WEBHOOK_SECRET']
DOMAIN = os.environ['DOMAIN']

# They submit a form with their email, physical address and type of product
@app.get("/buy")
def buy_credits(product=str, email=str, address=str):
  print(product, email, address)
  # TODO validate these inputs
  # Create Stripe Checkout Session
  price = 2496
  pn = f'You are buying a NotFriend ({product} version) - thank you for being a part of this!'
  s = stripe.checkout.Session.create(
      payment_method_types=['card'],
      metadata = {
        "product": product,
        "email":email,
        "address":address
      },
      line_items=[{
          'price_data': {
              'currency': 'usd',
              'unit_amount': price,
              'product_data': {
                  'name': pn,
              },
          },
          'quantity': 1,
      }],
      mode='payment',
      success_url=DOMAIN + '/success?session_id={CHECKOUT_SESSION_ID}',
      cancel_url=DOMAIN + '/cancel',
  )

  # Send the USER to STRIPE
  return RedirectResponse(s['url'])


# STRIPE sends the USER here after a payment was canceled.
@app.get("/cancel")
def cancel():
  return Title('Cancelled'), P(f'Cancelled.', A('Return Home', href='/'))


# STRIPE sends the USER here after a payment was 'successful'.
@app.get("/success")
def success():
  return Title('Success'), P(f'Success!', A('Return Home', href='/'))


# STRIPE calls this to tell APP when a payment was completed.
@app.post('/webhook')
async def stripe_webhook(request):
  print(request)
  print('Received webhook')
  payload = await request.body()
  payload = payload.decode("utf-8")
  signature = request.headers.get('stripe-signature')
  print(payload)

  # Verify the Stripe webhook signature
  try:
    event = stripe.Webhook.construct_event(payload, signature, webhook_secret)
  except ValueError:
    print('Invalid payload')
    return {'error': 'Invalid payload'}, 400
  except stripe.error.SignatureVerificationError:
    print('Invalid signature')
    return {'error': 'Invalid signature'}, 400

  # Handle the event
  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']
    print("Session completed", session)
    return {'status': 'success'}, 200

serve()