Title: Electronics Workbench Panel
Date: 2023-05-23
Category: Projects

> In the middle of COVID (2020), my need for an electronics workbench became more concrete. I was budget and space constrained, but had plenty of freetime and energy during lockdown. This was my attempt to address the need with a flexible, DIY solution. 

# Why DIY?

As someone still operating on the hobbyist level, I needed a a couple of basic instruments:

- Digital multimeter
- DC power supply
- Oscilloscope

A laboratory-grade set would be inappropriate for my setup, from both a cost and space perspective.

The multimeter was easy—I had an underused *Fluke 115* from Amazon, that already seemed like overkill for Arduino projects:

![Fluke 115](images/fluke_115.jpg)

Most oscilloscopes seemed out-of-reach. On Amazon, there are several entry-level models that. Another option 

# Gathering Components

![DCDC](images/uctronics_dcdc_converter.jpg)

![Meanwell](images/meanwell_edr_120_24.jpg)


# Design & Construction

| **Components** | **Unit Cost** | **Quantity** | **Subtotal** |
|:--------------:|:-------------:|--------------|--------------|
|                |               |              | $            |
|                |               |              | $            |
|                |               |              | $            |
|                |               | **Total**    | $            |

# Usage

The two-channel DC power supply immediately paid off. I was able to work on projects with mixed power needs, such as interfacing a 5 VDC Arduino with a 3.3V sensor breakout board. 

A simple convention that became convenient when working on the breadboards:
**RED** = 5 VDC, **YELLOW** = 3.3 VDC, and **BLACK** = GND.
