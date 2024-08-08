
from fasthtml.common import *
from fasthtml.svg import *

# Set up the app
tlink = Script(src="https://cdn.tailwindcss.com"),
app = FastHTML(hdrs=(tlink, ), pico=False)

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
                                A('Buy Now', href='#', cls='inline-flex h-9 items-center justify-center rounded-md bg-[#e74c3c] px-4 py-2 text-sm font-medium text-primary-foreground shadow transition-colors hover:bg-[#c0392b] focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50'),
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
            cls='w-full py-6 md:pt-12 lg:pt-18 border-y'
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
                cls='container space-y-12 px-4 md:px-6'
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
                                Div('- Jane Doe, NotFriend Enthusiast', cls='text-sm text-[#555]'),
                                cls='grid gap-2 text-left'
                            ),
                            cls='mx-auto flex w-full items-center justify-center p-4 sm:p-8'
                        ),
                        Div(
                            Div(
                                Div('"I can\'t imagine my life without my NotFriend."', cls='text-xl font-bold text-[#2c3e50]'),
                                Div('- John Smith, NotFriend Addict', cls='text-sm text-[#555]'),
                                cls='grid gap-2 text-left'
                            ),
                            cls='mx-auto flex w-full items-center justify-center p-4 sm:p-8'
                        ),
                        cls='grid w-full grid-cols-1 items-stretch justify-center divide-y md:grid-cols-2'
                    ),
                    cls='divide-y rounded-lg border border-[#2c3e50]'
                ),
                cls='container grid items-center justify-center gap-4 px-4 text-center md:px-6'
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
                            Div(
                                H3(
                                    Button(
                                        'What is the NotFriend?',
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
                                            cls='lucide lucide-chevron-down h-4 w-4 shrink-0 transition-transform duration-200'
                                        ),
                                        type='button',
                                        aria_controls='radix-:rj:',
                                        aria_expanded='false',
                                        data_state='closed',
                                        data_orientation='vertical',
                                        id='radix-:ri:',
                                        data_radix_collection_item='',
                                        cls='flex flex-1 items-center justify-between py-4 transition-all hover:underline [&[data-state=open]>svg]:rotate-180 bg-[#e67e22] text-[#2c3e50] font-bold'
                                    ),
                                    data_orientation='vertical',
                                    data_state='closed',
                                    cls='flex'
                                ),
                                Div(data_state='closed', id='radix-:rj:', hidden='', role='region', aria_labelledby='radix-:ri:', data_orientation='vertical', style='--radix-accordion-content-height: var(--radix-collapsible-content-height); --radix-accordion-content-width: var(--radix-collapsible-content-width);', cls='overflow-hidden text-sm transition-all data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down'),
                                data_state='closed',
                                data_orientation='vertical',
                                cls='border-b'
                            ),
                            Div(
                                H3(
                                    Button(
                                        'How does the NotFriend work?',
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
                                            cls='lucide lucide-chevron-down h-4 w-4 shrink-0 transition-transform duration-200'
                                        ),
                                        type='button',
                                        aria_controls='radix-:rl:',
                                        aria_expanded='false',
                                        data_state='closed',
                                        data_orientation='vertical',
                                        id='radix-:rk:',
                                        data_radix_collection_item='',
                                        cls='flex flex-1 items-center justify-between py-4 transition-all hover:underline [&[data-state=open]>svg]:rotate-180 bg-[#e67e22] text-[#2c3e50] font-bold'
                                    ),
                                    data_orientation='vertical',
                                    data_state='closed',
                                    cls='flex'
                                ),
                                Div(data_state='closed', id='radix-:rl:', hidden='', role='region', aria_labelledby='radix-:rk:', data_orientation='vertical', style='--radix-accordion-content-height: var(--radix-collapsible-content-height); --radix-accordion-content-width: var(--radix-collapsible-content-width);', cls='overflow-hidden text-sm transition-all data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down'),
                                data_state='closed',
                                data_orientation='vertical',
                                cls='border-b'
                            ),
                            Div(
                                H3(
                                    Button(
                                        'Why would I want a NotFriend?',
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
                                            cls='lucide lucide-chevron-down h-4 w-4 shrink-0 transition-transform duration-200'
                                        ),
                                        type='button',
                                        aria_controls='radix-:rn:',
                                        aria_expanded='false',
                                        data_state='closed',
                                        data_orientation='vertical',
                                        id='radix-:rm:',
                                        data_radix_collection_item='',
                                        cls='flex flex-1 items-center justify-between py-4 transition-all hover:underline [&[data-state=open]>svg]:rotate-180 bg-[#e67e22] text-[#2c3e50] font-bold'
                                    ),
                                    data_orientation='vertical',
                                    data_state='closed',
                                    cls='flex'
                                ),
                                Div(data_state='closed', id='radix-:rn:', hidden='', role='region', aria_labelledby='radix-:rm:', data_orientation='vertical', style='--radix-accordion-content-height: var(--radix-collapsible-content-height); --radix-accordion-content-width: var(--radix-collapsible-content-width);', cls='overflow-hidden text-sm transition-all data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down'),
                                data_state='closed',
                                data_orientation='vertical',
                                cls='border-b'
                            ),
                            Div(
                                H3(
                                    Button(
                                        'Can I actually buy this?',
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
                                            cls='lucide lucide-chevron-down h-4 w-4 shrink-0 transition-transform duration-200'
                                        ),
                                        type='button',
                                        aria_controls='radix-:rp:',
                                        aria_expanded='false',
                                        data_state='closed',
                                        data_orientation='vertical',
                                        id='radix-:ro:',
                                        data_radix_collection_item='',
                                        cls='flex flex-1 items-center justify-between py-4 transition-all hover:underline [&[data-state=open]>svg]:rotate-180 bg-[#e67e22] text-[#2c3e50] font-bold'
                                    ),
                                    data_orientation='vertical',
                                    data_state='closed',
                                    cls='flex'
                                ),
                                Div(data_state='closed', id='radix-:rp:', hidden='', role='region', aria_labelledby='radix-:ro:', data_orientation='vertical', style='--radix-accordion-content-height: var(--radix-collapsible-content-height); --radix-accordion-content-width: var(--radix-collapsible-content-width);', cls='overflow-hidden text-sm transition-all data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down'),
                                data_state='closed',
                                data_orientation='vertical',
                                cls='border-b'
                            ),
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
                cls='container px-4 md:px-6'
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
    return Title("NotFriend"), page

@app.get('/product_shot.jpeg')
def product_shot():
    return FileResponse('product_shot.jpeg')

serve()