Title: Electronics Workbench Panel
Date: 2023-05-23
Category: Projects
Summary:

> In the middle of COVID (2020), my need for an electronics workbench became more concrete. I was budget and space constrained, but had plenty of free time and energy during lockdown. This was my attempt to address the need with a flexible, DIY solution. 

# Why DIY?

As someone still operating on the hobbyist level, I needed a a couple of basic instruments:

- Digital multimeter
- DC power supply
- Oscilloscope

A laboratory-grade set would be inappropriate from both a cost and space perspective. At the time, I also lacked proper storage and shelving, and wanted a setup that hugged the edge of my long worktable. A custom setup could address this and potentially yield significant cost savings.

# Gathering Components

The multimeter was easy—I had an underused **Fluke 115** from Amazon, that already seemed like overkill for Arduino projects:

![Fluke 115](images/fluke_115.jpg)

At the time, most entry-level oscilloscopes (ex. Rigol, Siglent) on Amazon seemed too expensive ($300-$500). Analog scopes at the local electronics surplus store did not have the expected discount (>$100 used???) and seemed clunky. 

I settled on a cheap **DSO 138** kit, with unsoldered through-hole components for extra DIY fun. I knew you couldn't do serious work with it, but it seemed sufficient for probing digital communication lines and other simple tasks.

![DSO 138](images/dso_138_oscilloscope.jpg)

Finally, I started looking at DC power supplies. At minimum, I needed two channels and would've liked three. Again, the entry-level brand-name options were too expensive. Single channel options were cheaper but were insufficient

The only solution that met my cost and space needs were small, panel-mount units from **Uctronics** (available on Amazon):

![DCDC](images/uctronics_dcdc_converter.jpg)

It became clear that a custom panel would need to be designed & built to mount my instruments. This would require manual power distribution to each component, while considering their different voltage needs.

The last piece of the puzzle was the 

![Meanwell](images/meanwell_edr_120_24.jpg)

# Design & Construction

At Home Depot, a standard ### in board ### x ###. The board was divided as follows:

(FRONT)

(BACK)

Switches were used to toggle every major component:

- AC-DC Converter (i.e. Master Supply)
- DC-DC Converter (Ch. 1)
- DC-DC Converter (Ch. 2)
- Oscilloscope

(3D print bracket drawing here)

| **Components** | **Unit Cost** | **Quantity** | **Subtotal** |
|:--------------:|:-------------:|--------------|--------------|
|                |               |              | $            |
|                |               |              | $            |
|                |               |              | $            |
|                |               | **Total**    | $            |


# Usage

The two-channel DC power supply was immediately useful. I was able to work on projects with mixed power needs, such as interfacing a 5 VDC Arduino with a 3.3V sensor breakout board. 

A simple convention that became convenient when working on the breadboards:
**RED** = 5 VDC, **YELLOW** = 3.3 VDC, and **BLACK** = GND.

The supporting components---switches, barrel jacks, & fans etc.---were all problem free and I hade no complaints. If there was an imporvement to be made, I think the cooling scheme for the DC-DC converters could've been more robust. I'm unsre of how effective the ventilation holes were and a proper air duct (3D-printed) was probably the better solution.

The main letdown was the oscilloscope. While the limited functions & small screen size weren't major issues, the poor viewing angle was. The screen could only be viewed head-on and overall was not ergonomic to view when working.
