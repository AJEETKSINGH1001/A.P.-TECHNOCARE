Production-Ready Django B2B Business Website — Master Prompt Pack


0. How to use this prompt pack
Run Prompt 00 first, then run Prompts 01–29 in order against the same repository. These prompts are written for a coding agent such as Cursor, Claude Code, Codex, or an IDE agent with filesystem/terminal access.
Replace the variables below before the first implementation pass:
`{{BUSINESS_NAME}}`
`{{DOMAIN}}`
`{{PRIMARY_CITY}}`
`{{PRIMARY_STATE}}`
`{{COUNTRY}}`
`{{PRIMARY_PHONE}}`
`{{PRIMARY_EMAIL}}`
`{{WHATSAPP_NUMBER}}`
`{{BUSINESS_DESCRIPTION}}`
`{{PRIMARY_BRAND_COLOR}}`
`{{SECONDARY_BRAND_COLOR}}`
`{{LOGO_PATH_OR_ASSET}}`
`{{GOOGLE_MAPS_URL}}`
`{{SOCIAL_LINKS}}`
Default architecture: server-rendered Django first, progressively enhanced with HTMX and Alpine.js; PostgreSQL for production; Redis for cache/background work; Tailwind CSS for the design system; Django REST Framework for APIs/integrations; object storage for media; Docker for local/production parity; automated tests, CI/CD, observability, backups, and security hardening.
As of 2026-10-02, Django 6.1.1 is the latest released patch visible in the official release notes. Django 6.1 supports Python 3.12, 3.13, and 3.14. Use the latest stable security/bugfix release available on the actual implementation date, pin dependencies, and verify compatibility before installation.
---
SOURCE-BASED REFERENCE MODEL
The supplied website is an IndiaMART-style B2B seller storefront. The source shows:
A company header with business name, city/state, GST information, trust/verification badge, phone CTA, response-rate indicator, and email CTA.
A main navigation with “Our Product Range”, “About Us”, “Testimonial”, and “Contact Us”, plus a product search field and a sticky CTA that appears on scroll.
Eight visible top-level product/category tiles: Welding Electrode, Safety Shoes, 3M Safety Mask, Plasma Consumables, Lubricant Spray, Safety Helmet, Safety Goggles, and Ear Protection.
A featured/hero area with product cards and repeated “Get Latest Price” / “Get Quote” interactions.
An “About” section with structured business facts such as nature of business, employee count, registration date, legal status, turnover, IEC, GST number, and verification state.
A product-range section that repeats a category heading, “View All”, product cards, product image, product title, specification bullets, “Get Latest Price”, and “Get Quote”.
A contact section with address, directions, email, phone, social sharing, and an enquiry form.
A footer with company links, product-range links, social links, legal text, sitemap, and an enquiry form.
Structured data using LocalBusiness JSON-LD, plus canonical, Open Graph, Twitter, robots, description, and keyword metadata.
Analytics/event instrumentation and lazy-loaded external assets.
The source relies on legacy hosted CSS/JS, inline event handlers, hardcoded seller data, and external IndiaMART infrastructure. Rebuild these behaviors as first-party Django capabilities rather than carrying the legacy implementation across.
Do not copy proprietary source code, third-party hosted CSS/JS, tracking identifiers, external seller assets, trademarks that the business does not have permission to use, or source text verbatim. Re-create the information architecture and useful interaction patterns with original implementation, original branding, and assets supplied by the business.
---
PROMPT 00 — MASTER PROJECT ORCHESTRATOR
You are the lead software architect, senior Django engineer, frontend engineer, UX engineer, SEO engineer, DevOps engineer, security engineer, QA lead, and technical writer for this repository.
Build a production-ready B2B business website for:
Business: {{BUSINESS_NAME}}
Domain: {{DOMAIN}}
Primary location: {{PRIMARY_CITY}}, {{PRIMARY_STATE}}, {{COUNTRY}}
Business domain: industrial/safety/welding/MRO products and related B2B enquiries
Primary conversion: enquiry / quote request / call / WhatsApp / email
Framework: Python + Django
Frontend strategy: Django templates + Tailwind CSS + HTMX + Alpine.js
Database: PostgreSQL
Cache/queues: Redis
API layer: Django REST Framework
Media: S3-compatible object storage
Deployment: Docker + reverse proxy + HTTPS + managed PostgreSQL/Redis
CI: GitHub Actions
Quality: Ruff, MyPy where practical, pytest, Django tests, Playwright for critical browser flows
Observability: structured logs + Sentry + optional OpenTelemetry
DNS/CDN/WAF: Cloudflare or equivalent
Operating rules:
Inspect the repository before changing anything.
Never invent secrets or production credentials.
Never hardcode business secrets into source control.
Use environment variables and typed configuration.
Prefer small, testable modules over giant views/templates.
Use Django ORM; avoid raw SQL unless justified and tested.
Use database constraints, indexes, transactions, and validation.
Use accessible semantic HTML.
Use responsive/mobile-first layouts.
Preserve canonical URLs and build explicit redirect support where legacy URLs matter.
Do not make a claim of completion without running tests/checks.
Every implementation task must end with:
summary of changes
files changed
commands executed
test results
security/performance notes
remaining TODOs
When information is missing, create clearly marked content placeholders and a CONTENT_REQUIRED.md checklist instead of blocking the build.
Do not ask unnecessary clarification questions; make reasonable reversible defaults.
Do not replace working features merely to use a newer technology.
Keep frontend JavaScript minimal; progressively enhance server-rendered HTML.
Make all important business content editable from Django admin.
Ensure image handling uses responsive, optimized formats and safe upload validation.
All enquiry flows must have CSRF, server-side validation, rate limiting/abuse protection, spam controls, audit trail, status, and notification handling.
Treat SEO, security, accessibility, performance, backup/recovery, observability, and deployment as first-class requirements.
Definition of done:
`python manage.py check --deploy` is clean or all remaining warnings are explicitly documented and justified.
Migrations are deterministic.
Automated tests cover critical paths.
Static assets build successfully.
Production settings are separated from local settings.
No secrets are committed.
HTTPS, secure cookies, CSP, HSTS, CSRF, permissions, upload limits, and security headers are intentionally configured.
Search, catalog, enquiry, contact, admin, SEO, and observability workflows are usable.
Mobile and desktop critical flows have been tested.
Deployment and rollback are documented.
---
PROMPT 01 — REVERSE-ENGINEER THE REFERENCE SOURCE
Analyze the supplied HTML reference and create a formal implementation specification.
Tasks:
Parse the full source file.
Inventory:
page metadata
navigation
category structure
product card structure
product specifications
CTA behaviors
enquiry fields
footer structure
contact blocks
social sharing
structured data
analytics/events
responsive behavior
sticky behavior
lazy-loading behavior
Separate:
functional requirements
visual patterns
content/data requirements
third-party dependencies
legacy implementation details
Produce:
`docs/reference-audit.md`
`docs/feature-matrix.md`
`docs/url-inventory.md`
`docs/reference-data-inventory.md`
Mark each item as:
MUST HAVE
SHOULD HAVE
OPTIONAL
REPLACE WITH MODERN APPROACH
Explicitly identify source-specific pieces that must NOT be copied, such as third-party tracking IDs or externally hosted implementation assets.
Do not implement the website yet. Produce a complete implementation blueprint first.
---
PROMPT 02 — BUSINESS CONTENT CONTRACT
Create a content/data contract for {{BUSINESS_NAME}}.
Create:
`docs/content-contract.md`
`docs/content-required.md`
`fixtures/content_seed.json` where useful
Define canonical fields for:
business name
tagline
short description
full company description
logo
favicon
brand colors
phone
email
WhatsApp
address
map URL
business hours
social links
GST details
legal information
employee range
establishment/registration date
turnover range
IEC
certifications
trust/verification wording
payment methods
shipping/service coverage
service areas
brands represented
product categories
product facts/specifications
FAQs
testimonials
homepage featured products
SEO titles/descriptions
schema.org fields
Where exact content is unknown, use placeholders and never fabricate legal/business claims.
---
PROMPT 03 — SITEMAP, UX, ROUTES, AND URL POLICY
Design the complete information architecture.
Required public pages:
`/`
`/products/`
`/products/<category-slug>/`
`/products/<category-slug>/<product-slug>/`
`/search/`
`/about/`
`/testimonials/`
`/contact/`
`/enquiry/`
`/privacy/`
`/terms/`
`/refund-policy/` if relevant
`/shipping-policy/` if relevant
`/sitemap.xml`
`/robots.txt`
Support:
legacy `.html` aliases/redirects if required
canonical URLs
trailing-slash policy
slug normalization
301 redirect registry
404 page
410 support for intentionally removed content
pagination
query-string preservation where SEO-safe
Create:
route map
navigation map
breadcrumbs
mobile navigation
footer map
conversion journey from landing page to enquiry
Deliver:
`docs/information-architecture.md`
`docs/url-policy.md`
---
PROMPT 04 — DESIGN SYSTEM AND RESPONSIVE UX
Create an original design system inspired only by the useful structure of the reference.
Requirements:
modern B2B/industrial visual language
strong product photography
high contrast CTAs
restrained use of color
typography scale
card system
buttons
badges
forms
chips
alerts
breadcrumbs
pagination
modal/drawer
sticky CTA
loading states
skeleton states
empty states
error states
toast/feedback states
mobile bottom CTA if appropriate
Use Tailwind CSS with a small project-specific design token layer.
Create:
colors
spacing
radius
shadows
typography
breakpoints
layout containers
component naming rules
Accessibility:
WCAG-oriented contrast
visible focus
keyboard navigation
semantic landmarks
reduced motion support
touch target sizing
Deliver:
`docs/design-system.md`
component-level CSS/token implementation
Storybook only if the team actually needs it; otherwise use a Django component/demo page.
---
PROMPT 05 — CREATE THE DJANGO PROJECT FOUNDATION
Initialize or refactor the repository into a clean production-oriented Django project.
Recommended app boundaries:
`core`
`pages`
`catalog`
`leads`
`reviews`
`seo`
`analytics`
`accounts`
`api`
Use a clear configuration structure:
`config/settings/base.py`
`config/settings/local.py`
`config/settings/staging.py`
`config/settings/production.py`
Set:
timezone
language
templates
static files
media
email
logging
cache
sessions
security
database
middleware
storage
allowed hosts
CSRF trusted origins
Add:
`.env.example`
`pyproject.toml`
`.editorconfig`
`.gitignore`
pre-commit config
README
Makefile/task runner if useful
Use typed Python, clear imports, and deterministic dependency pinning.
---
PROMPT 06 — DEVELOPMENT ENVIRONMENT, CONTAINERS, AND CONFIGURATION
Create local development infrastructure.
Requirements:
Dockerfile
docker-compose/compose setup
PostgreSQL
Redis
Django app
optional mail catcher for local development
healthcheck endpoint
static/media development support
Create safe environment-variable loading.
Add separate configuration for:
local
test
staging
production
Never store production credentials in compose files.
Add developer commands for:
migrations
test
lint
format
type checks
build CSS
collectstatic
create superuser
load seed data
Document exact startup steps.
---
PROMPT 07 — DATABASE MODEL AND DOMAIN DESIGN
Implement a normalized B2B catalog and lead-management schema.
At minimum create:
`SiteSettings`
singleton behavior
business identity
contact details
address
branding
defaults
`Category`
name
slug
parent
description
image
SEO fields
is_active
sort_order
featured
`Product`
category
name
slug
SKU/code
short description
full description
price
price visibility enum
enquiry enabled
featured
active
brand
model
minimum order quantity if applicable
lead time if applicable
sort order
created/updated timestamps
`ProductImage`
product
image
alt text
caption
sort order
primary flag
`ProductSpecification`
product
name
value
normalized key
sort order
`Brand`
name
slug
logo
description
`Tag`
name
slug
`Testimonial`
name
company
role
quote
rating only when legitimately sourced
approved
published_at
`Enquiry`
UUID/public ID
product nullable
category nullable
customer name
company
phone
email
message
source page
referrer
UTM fields
consent timestamp
IP hash or privacy-safe abuse key
user agent summary where needed
status
priority
assigned staff
created/updated timestamps
`EnquiryItem` for multi-product enquiries.
`EnquiryActivity`
enquiry
actor
event
note
timestamps
`SEOPage`
path or content object relationship
title
meta description
canonical
robots
OG image
schema JSON where appropriate
`Redirect`
source
destination
status code
active
`ContactPoint`
label
value
type
priority
active
Add database indexes and constraints deliberately.
Do not store secrets or payment card data.
---
PROMPT 08 — DJANGO ADMIN / MINI CMS
Turn Django admin into a usable business CMS.
Implement:
category management
product CRUD
bulk product activation/deactivation
featured product control
inline specifications
image management
testimonial moderation
enquiry management
status workflow
assignment
activity history
SEO metadata editing
redirect management
site settings
navigation/footer links
FAQ management
import/export for catalog data
Improve admin UX:
list filters
search
date hierarchy where useful
autocomplete fields
read-only audit data
sensible list displays
safe delete behavior
permissions by role
Define roles:
Super Admin
Content Manager
Sales/Enquiry Manager
Read-only Analyst
Add object-level permissions only where justified.
---
PROMPT 09 — MEDIA, IMAGE OPTIMIZATION, AND STORAGE
Implement a production media pipeline.
Requirements:
S3-compatible storage in production
local storage in development
validated upload types
safe file size limits
filename sanitization
automatic image dimensions
responsive image variants
WebP/AVIF where practical
lazy loading
width/height attributes to prevent layout shift
meaningful alt text
primary image selection
image cleanup when records are removed
Never trust MIME type alone.
Prevent:
executable uploads
SVG execution risks unless intentionally sanitized
path traversal
oversized image decompression attacks
unbounded uploads
---
PROMPT 10 — BASE LAYOUT, HEADER, NAVIGATION, FOOTER
Implement the shared application shell.
Header should include:
logo
business name
location
trust/certification badge area when applicable
click-to-call
email CTA
WhatsApp CTA
primary product navigation
search
responsive mobile menu
Navigation should support:
category mega-menu on desktop
accessible disclosure menu on mobile
nested categories
active states
keyboard operation
Footer should include:
company links
product categories
contact details
social links
legal links
copyright
optional newsletter/lead capture where appropriate
Implement:
sticky header only when UX benefits
sticky enquiry CTA on scroll
back-to-top control
reduced-motion behavior
Avoid inline JavaScript event handlers.
---
PROMPT 11 — HOMEPAGE
Implement the homepage as a data-driven Django template.
Sections:
header/navigation
category strip
hero/featured product area
popular products / featured products
product-range sections grouped by category
company introduction
business facts
trust/certification section
testimonials
service/coverage section
contact/CTA section
footer enquiry form
footer
Every section must be editable or configurable from admin where sensible.
Product cards should support:
image
title
short specs
price or “Get Latest Price”
“Get Quote”
detail page link
Use reusable template components rather than duplicating markup.
---
PROMPT 12 — CATEGORY / PRODUCT LISTING PAGES
Build:
`/products/`
and `/products/<category-slug>/`
Features:
responsive grid
category sidebar on desktop
mobile filter drawer
breadcrumbs
sort
pagination
filters
search within category
brand filter
attribute/specification filters when data is structured
price visibility rules
enquiry CTA
empty state
no-results state
SEO:
crawlable pagination where appropriate
canonical URLs
unique title/meta
structured category content
category schema only where valid
Performance:
`select_related`
`prefetch_related`
pagination
database indexes
no N+1 queries
---
PROMPT 13 — PRODUCT DETAIL PAGE
Create a strong B2B product-detail experience.
Include:
product title
primary image
gallery
product code/SKU
price or enquiry state
key specifications
full description
brands/models
documents/brochures where applicable
enquiry CTA
call CTA
WhatsApp CTA
share button
related products
related categories
breadcrumbs
FAQ section when relevant
Interaction:
image lightbox
thumbnail gallery
sticky mobile enquiry CTA
enquiry modal/drawer
HTMX submission with graceful full-page fallback
Use schema.org Product only when sufficient product data exists. Avoid fake reviews/prices/availability.
---
PROMPT 14 — SEARCH, AUTOCOMPLETE, AND FILTERING
Implement first-party search.
Phase 1:
PostgreSQL full-text/trigram search as justified
product title
SKU/code
brand
category
structured specification values
Autocomplete:
debounced request
top matches
category match
product match
keyboard support
no-results state
rate limit
Search results:
relevant ranking
spelling-tolerant behavior where feasible
pagination
filters
query persistence
Do not expose internal unpublished content.
Design the search service so an external engine such as Meilisearch/OpenSearch can be added later without rewriting the UI.
---
PROMPT 15 — B2B ENQUIRY / QUOTE SYSTEM
Implement the main conversion engine.
Flows:
“Get Quote”
“Get Latest Price”
“Contact Us”
footer enquiry form
product-specific enquiry
category-specific enquiry
general enquiry
Fields:
name
company
phone
email
requirement
product
quantity/unit when useful
consent
optional attachment
Requirements:
CSRF
server-side validation
normalize phone/email
anti-spam
honeypot
rate limit
optional CAPTCHA only when needed
duplicate/submission throttling
audit trail
source URL
referrer
campaign/UTM capture
status workflow
staff assignment
email notification
optional WhatsApp/SMS notification
customer acknowledgement
Statuses:
New
Contacted
Qualified
Quoted
Won
Lost
Spam
Closed
Add admin filters and a lightweight sales pipeline view.
---
PROMPT 16 — ABOUT, TESTIMONIALS, CONTACT, AND BUSINESS TRUST
Implement:
About page
Testimonials page
Contact page
About page:
business story
capabilities
product categories
brands
business facts
certifications
service areas
why customers contact the business
enquiry CTA
Testimonials:
moderated publishing
no fake testimonials
optional rating only from legitimate source data
Contact:
address
map/directions
hours
phone
email
WhatsApp
enquiry form
social links
privacy notice
Keep legal/company facts editable in admin and sourced from authoritative business records.
---
PROMPT 17 — SEO, METADATA, STRUCTURED DATA, AND INDEXING
Implement technical SEO from the beginning.
Page-level:
unique title
meta description
canonical
robots
Open Graph
Twitter card
OG image
language
favicon
clean slugs
breadcrumbs
Schema where accurate:
Organization/LocalBusiness
PostalAddress
WebSite
BreadcrumbList
Product
AggregateRating only from legitimate, verifiable reviews
FAQPage only when visible FAQ content meets search-engine requirements
Generate:
XML sitemap
robots.txt
canonical URLs
redirect handling
404
410 where appropriate
Add:
SEO preview fields in admin
default fallbacks
image metadata
noindex for internal/admin/search pages when appropriate
Never fabricate ratings, reviews, business facts, product prices, or availability.
---
PROMPT 18 — ANALYTICS, CONSENT, AND CONVERSION EVENTS
Replace legacy inline analytics with a clean event layer.
Track at minimum:
page_view
search
category_view
product_view
enquiry_open
enquiry_submit
enquiry_success
click_to_call
click_to_email
click_to_whatsapp
get_quote
get_latest_price
directions_click
social_share
Requirements:
no hardcoded external tracking identifiers
settings-driven analytics IDs
consent-aware behavior where required
no leakage of enquiry PII into analytics
server-side logging for business-critical conversion events
clear event naming conventions
optional GA4 integration
optional server-side analytics
Create:
`docs/analytics-events.md`
---
PROMPT 19 — NOTIFICATIONS AND EXTERNAL INTEGRATIONS
Implement a provider abstraction for:
email
transactional notifications
optional SMS
optional WhatsApp
optional CRM/webhook integration
Requirements:
asynchronous background jobs
retry policy
exponential backoff
idempotency
dead-letter/error logging where provider supports it
admin-visible delivery status
no secrets in logs
provider swap without changing business logic
Example use cases:
new enquiry notification to sales
customer acknowledgement
enquiry assignment notification
daily summary
webhook to CRM
---
PROMPT 20 — API LAYER
Expose a versioned internal/public API using Django REST Framework where useful.
Start with:
categories
products
product detail
search
enquiry create
enquiry status for authenticated staff
testimonials
site configuration only for public-safe fields
Requirements:
`/api/v1/`
serializers
validation
pagination
throttling
authentication for private endpoints
permissions
OpenAPI schema
API documentation
stable error format
Do not expose unpublished or internal business data.
---
PROMPT 21 — PERFORMANCE, CACHING, AND CORE WEB VITALS
Optimize the application before deployment.
Requirements:
database indexes
query counting on critical views
`select_related/prefetch_related`
pagination
cache public pages/fragments where safe
Redis cache
HTTP caching headers
compressed responses
optimized images
responsive images
lazy loading below the fold
defer noncritical JavaScript
minimize third-party scripts
preconnect only when justified
prevent layout shifts
font loading strategy
asset hashing
Performance budgets:
define target TTFB
define LCP/INP/CLS budgets
define JS/CSS budgets
define image weight targets
Create a repeatable performance test script/process.
Be especially careful with cached pages that include session or personalized data.
---
PROMPT 22 — SECURITY HARDENING
Perform a production security review.
Configure and verify:
`DEBUG=False`
`ALLOWED_HOSTS`
`CSRF_TRUSTED_ORIGINS`
secure cookies
HTTPOnly cookies
SameSite policy
HSTS
secure redirects
X-Content-Type-Options
Referrer-Policy
Permissions-Policy
Content-Security-Policy
frame protections
clickjacking protection
upload restrictions
request size limits
rate limiting
login throttling
admin URL hardening only as defense-in-depth
least-privilege permissions
secret rotation procedure
dependency audit
For Django CSP, use the built-in CSP support available in modern Django rather than inventing custom middleware unless necessary.
Audit:
XSS
CSRF
SQL injection
SSRF
path traversal
insecure file uploads
open redirects
mass assignment
IDOR
session fixation
sensitive logging
information disclosure
Run automated dependency/security scanners.
---
PROMPT 23 — ACCESSIBILITY, MOBILE, AND BROWSER QA
Test all core flows on:
small mobile
large mobile
tablet
laptop
desktop
Critical flows:
navigation
category browse
search
product detail
enquiry
call
email
WhatsApp
contact form
admin login
product creation
product editing
Accessibility:
keyboard-only
screen-reader semantics
focus management
form labels/errors
modal focus trap
color contrast
alt text
reduced motion
headings hierarchy
Use Playwright for browser-level tests of the highest-value paths.
---
PROMPT 24 — AUTOMATED TESTING AND RELEASE QUALITY
Build a complete test suite.
Unit tests:
models
validators
slug logic
business rules
services
search ranking
enquiry deduplication/rate limit helpers
Integration tests:
views
forms
admin
email notification workflows
API endpoints
sitemap
redirects
Browser tests:
homepage
category
product
search
enquiry success
enquiry validation
mobile navigation
Security tests:
unauthorized admin/API access
CSRF
upload validation
rate limits
open redirect protections
CI must fail on:
test failures
migrations not applied
lint failures
type-check failures where configured
broken asset build
missing required environment variables in CI test mode
---
PROMPT 25 — OBSERVABILITY, LOGGING, BACKUPS, AND DISASTER RECOVERY
Implement production observability.
Logs:
JSON/structured logs
request ID
correlation ID
severity
safe context
no PII leakage
Errors:
Sentry or equivalent
deployment release tagging
source maps where needed
alert thresholds
Metrics:
request count
latency
error rate
DB pool saturation
cache hit rate
enquiry submissions
background job failures
Health endpoints:
liveness
readiness
database
Redis
storage dependency where appropriate
Backups:
automated database backup
retention policy
object storage versioning where available
documented restore procedure
restore test
Write:
`docs/operations.md`
`docs/disaster-recovery.md`
---
PROMPT 26 — CI/CD PIPELINE
Implement GitHub Actions.
Pipeline stages:
checkout
install dependencies
lint
format check
type checks where enabled
tests
security audit
CSS/static build
collectstatic/test
Docker build
image scan
deploy to staging
smoke tests
production approval/deploy
post-deploy smoke tests
Use:
dependency caching
reproducible lock/pin strategy
environment-specific secrets
artifact retention
migration safety checks
Never auto-run destructive migrations or data deletion.
---
PROMPT 27 — PRODUCTION DEPLOYMENT
Create a deployment architecture for:
Django ASGI app
reverse proxy/load balancer
PostgreSQL
Redis
object storage
CDN/WAF
background worker
scheduler if needed
Options may include:
managed container platform
VPS
Kubernetes only if scale/team actually requires it
Prefer the simplest architecture that satisfies:
availability
security
backups
scaling
observability
cost control
Production checklist:
domain
DNS
TLS certificate
email DNS
SPF/DKIM/DMARC
environment variables
database
cache
storage
static assets
scheduled jobs
monitoring
backups
restore plan
admin access
robots/sitemap
analytics
consent/privacy
redirects
Document:
deployment
rollback
migration process
incident response
scaling
---
PROMPT 28 — PRE-LAUNCH / GO-LIVE AUDIT
Run a formal launch audit.
Verify:
all pages render
all important links work
all forms work
all enquiry notifications arrive
email sending works
WhatsApp/call/email links work
sitemap is valid
robots.txt is valid
canonical URLs are correct
OG tags are correct
schema JSON is valid
no placeholder content remains
no test accounts are exposed
no development endpoints are public
no debug pages are public
no secrets are leaked
uploads are safe
backups have been tested
error monitoring works
analytics events work without PII leakage
mobile layout is clean
keyboard navigation works
Run:
Django deployment checks
dependency scan
browser smoke tests
performance test
link checker
HTML validation where practical
Create a launch report with PASS/FAIL/ATTENTION items.
---
PROMPT 29 — HANDOFF, DOCUMENTATION, AND MAINTENANCE
Prepare the system for another developer or business operator.
Create:
`README.md`
`docs/architecture.md`
`docs/local-development.md`
`docs/deployment.md`
`docs/environment.md`
`docs/admin-guide.md`
`docs/catalog-management.md`
`docs/enquiry-workflow.md`
`docs/seo-guide.md`
`docs/analytics-events.md`
`docs/security.md`
`docs/operations.md`
`docs/disaster-recovery.md`
`docs/troubleshooting.md`
`CHANGELOG.md`
Document:
architecture decisions
app responsibilities
URL policy
data model
admin roles
content editing
deployment
rollback
backup restore
common failures
third-party integrations
dependency update policy
Add a maintenance cadence:
security updates
dependency updates
backup restore tests
performance review
SEO/content review
analytics review
---
PROMPT 30 — OPTIONAL MODERN ENHANCEMENTS AFTER CORE LAUNCH
Only implement these after the core site is stable.
Candidate enhancements:
multi-language content
B2B account/customer portal
saved enquiries
multi-product quote basket
product comparison
downloadable technical catalog
PWA/offline brochure access
AI-assisted site search
AI enquiry classification
CRM sync
ERP inventory/price sync
supplier/brand catalog feeds
advanced search engine
recommendation engine
dealer/distributor locator
service-area landing pages
marketing automation
customer-specific pricing
quote PDF generation
electronic quotation approval workflow
Rule:
Do not add these just because they are modern. Add them only when they map to a concrete business requirement and have an owner, acceptance criteria, security review, and operating cost estimate.
---
CROSS-CUTTING IMPLEMENTATION CHECKLIST
Engineering
[ ] Type hints
[ ] Small services
[ ] Transactions
[ ] Constraints
[ ] Indexes
[ ] Query optimization
[ ] Reusable templates/components
[ ] No duplicated business logic
[ ] No inline JS for core behavior
[ ] No secrets in repo
UX
[ ] Responsive
[ ] Accessible
[ ] Search
[ ] Sticky CTA
[ ] Product detail
[ ] Quote flow
[ ] Clear error states
[ ] Fast mobile experience
Catalog
[ ] Categories
[ ] Nested categories
[ ] Products
[ ] Specifications
[ ] Brands
[ ] Images
[ ] Featured products
[ ] Related products
[ ] Import/export
Leads
[ ] Enquiry model
[ ] Validation
[ ] Rate limit
[ ] Spam prevention
[ ] Notification
[ ] Staff workflow
[ ] Audit history
[ ] Source attribution
SEO
[ ] Titles
[ ] Meta descriptions
[ ] Canonicals
[ ] OG/Twitter
[ ] Sitemap
[ ] Robots
[ ] Breadcrumbs
[ ] Schema
[ ] Redirects
[ ] 404/410
Security
[ ] CSRF
[ ] CSP
[ ] HSTS
[ ] Secure cookies
[ ] Upload validation
[ ] Rate limiting
[ ] Least privilege
[ ] Dependency scanning
[ ] Secret management
[ ] Audit logging
Performance
[ ] Image optimization
[ ] Caching
[ ] DB indexes
[ ] No N+1
[ ] Asset compression
[ ] JS minimization
[ ] Core Web Vitals budget
[ ] Load test
[ ] CDN
Operations
[ ] Health checks
[ ] Sentry
[ ] Logs
[ ] Backups
[ ] Restore test
[ ] CI/CD
[ ] Staging
[ ] Rollback
[ ] Incident docs
---
RECOMMENDED INITIAL REPO STRUCTURE
```text
project/
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── local.py
│   │   ├── test.py
│   │   ├── staging.py
│   │   └── production.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── apps/
│   ├── core/
│   ├── pages/
│   ├── catalog/
│   ├── leads/
│   ├── reviews/
│   ├── seo/
│   ├── analytics/
│   ├── accounts/
│   └── api/
├── templates/
│   ├── base.html
│   ├── components/
│   ├── pages/
│   ├── catalog/
│   ├── leads/
│   └── errors/
├── static/
│   ├── src/
│   └── dist/
├── media/
├── fixtures/
├── docs/
├── scripts/
├── tests/
├── Dockerfile
├── compose.yml
├── pyproject.toml
├── manage.py
└── README.md
```
---
DEFINITION OF PRODUCTION READY
Do not call the website “production ready” until:
All functional requirements are implemented and tested.
All business content is real or explicitly marked as pending.
All critical conversion paths work on mobile and desktop.
Admin users can maintain categories, products, specifications, images, SEO, testimonials, and enquiries without code edits.
Search returns useful results.
Enquiries are validated, protected against abuse, stored, audited, and delivered to the business.
Error monitoring and structured logs are active.
Backups exist and a restore has been tested.
CI blocks regressions.
Production security settings are verified.
SEO files/schema are valid.
Performance meets agreed budgets.
Deployment and rollback are documented.
No third-party source implementation is required for the core site to function.