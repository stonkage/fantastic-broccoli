## Glance Catppuccin Frappe CSS

This project integrates the Glance [Catppuccin Frappe theme](https://github.com/glanceapp/glance/blob/v0.6.2/docs/themes.md) into:

- [Homepage](https://gethomepage.dev/)
- [Uptime-Kuma](https://github.com/louislam/uptime-kuma)
- [Material for Mkdocs](https://squidfunk.github.io/mkdocs-material/) 

Homepage elements have been documented so you can go with your own theme if you choose, mkdocs and kuma both work but there may be some elements that look little off.

---

## Installation

### Homepage
- Copy homepage.css to your homepage config folder
- Rename to custom.css
- Restart your homepage instance
- Ensure you choose slate as the your homepage theme

### Material for MKdocs
- Copy mkdocs.css to [stylesheets](https://squidfunk.github.io/mkdocs-material/customization/?h=css#additional-css) folder
- Rename to extra.css
- update mkdocs yaml folder to include [extra.css](https://squidfunk.github.io/mkdocs-material/customization/?h=css#additional-css) file
- Restart your mkdocs instance

### Uptime-Kuma Status Page
- Copy the contents of kuma.css
- Create and edit a status page
- Paste into custom.css section 

You can further integrate your apps by using the [iframe widget](https://github.com/glanceapp/glance/blob/v0.6.2/docs/configuration.md#iframe) in glance (see screenshots)

---

## Screenshot Examples

Glance Start Page
![Screenshot](https://github.com/stonkage/fantastic-broccoli/blob/main/screenshots/glance.png)

Homepage
![Screenshot from 2025-01-02 10-45-01](https://github.com/user-attachments/assets/2bda7047-9310-465d-b22f-8f4a502ce039)

Material for MKdocs
![Screenshot from 2025-01-02 11-04-40](https://github.com/user-attachments/assets/83ca6418-0248-4b4d-a0d2-99b36f98fc1d)

Uptime Kuma
![Screenshot from 2025-01-02 11-05-18](https://github.com/user-attachments/assets/1e3e31ec-ade9-452b-bfaf-195eedb1a5ba)





