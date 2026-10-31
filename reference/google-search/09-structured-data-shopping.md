# Structured data: Shopping: Google Search documentation notes

Source: Google Search Central documentation (developers.google.com), retrieved 2026-10-31. © Google, licensed under CC BY 4.0. Summarized and restructured; not an official Google document.

## Overview (Introduction to `Product` structured data)
https://developers.google.com/search/docs/appearance/structured-data/product · Last updated: 2025-12-10

### Effect and scope
- `Product` markup can enrich product results in Google Search, Google Images and Google Lens: price, availability, review ratings, shipping info and more.
- Experiences listed (not exhaustive, may change): product snippet (text result with ratings, review info, price, availability), popular products (visual presentation), shopping knowledge panel (product details plus seller list using identifiers), Google Images (annotated product images).

### Choosing the markup class
- Product snippets: for pages where people cannot buy the product directly. More review options (for example pros and cons on editorial reviews).
- Merchant listings: for pages where customers can buy from you. More product-detail options (apparel sizing, shipping, return policy).
- Overlap: the required merchant-listing properties generally also make a page eligible for product snippets. Each feature has its own enhancements; more properties means more eligible enhancements.
- Variants: add product variant markup (`ProductGroup`) so Google knows which products are variations of one parent. Supported by both snippets and merchant listings.
- Business-level policies: also recommended, nested under `Organization` markup: merchant return policy (`MerchantReturnPolicy`), loyalty program (`MemberProgram`). The shipping policy page adds `ShippingService` the same way.

### Result enhancements
- Shown at the discretion of each experience and may change; provide as much product data as available.
- Ratings: customer reviews and ratings.
- Pros and cons: put them in an editorial product review so they can be highlighted.
- Shipping: share costs, especially free shipping.
- Availability: stock info.
- Price drop: computed by Google from observed price changes over time. Not guaranteed to show.
- Returns: policy, fees, number of return days.

### Data channels
- Two channels: `Product` structured data on pages, and a Google Merchant Center feed (with opt-in to free listings in the Merchant Center console). The Search Central docs cover only on-page markup.
- Using both maximizes eligibility and helps Google verify the data. Some experiences combine both sources; for example, product snippets may take the price from the feed when the page markup lacks it.
- Shopping tab eligibility is governed by Merchant Center data and eligibility requirements, not by these pages.

## Product snippet (`Product`, `Review`, `Offer`)
https://developers.google.com/search/docs/appearance/structured-data/product-snippet · Last updated: 2026-09-08

### Purpose
- `Product` markup can produce a product snippet: a text result with ratings, review information, price and availability.
- For pages where customers can purchase, the merchant listing guide is the better fit.

### How to add structured data (shared workflow)
- Add the required properties in a supported format. A CMS plugin or JavaScript generation are both possible.
- Follow the guidelines.
- Validate with the Rich Results Test. Fix critical errors; non-critical warnings are optional for eligibility but improve quality.
- Deploy a few pages, then use URL Inspection to confirm Google sees them. The page must not be blocked by robots.txt, `noindex` or a login requirement. Then request recrawl. Allow several days.
- Submit a sitemap to keep Google informed of changes (can be automated with the Search Console Sitemap API).

### Examples (key lessons)
- Product review page: `Product` with `name`, `review` (with `reviewRating` and `author`), `aggregateRating`; may add `offers` (`Offer`), `image`, `sku`, `mpn`, `brand`.
- Pros and cons example: an editorial review page. Nested `review` carries `positiveNotes` and `negativeNotes` as `ItemList` of `ListItem` (`position`, `name`).
- Shopping aggregator example: `offers` is an `AggregateOffer` (`offerCount`, `lowPrice`, `highPrice`, `priceCurrency`) rather than a single `Offer`.
- Formats shown: JSON-LD, RDFa, Microdata.
> Note: the aggregator Microdata sample uses `offerCount` 6 while the JSON-LD sample uses 5. Sample inconsistency only.

### Technical guidelines
- Only pages focused on a single product (or several variants of one product) are supported. "Shoes in our shop" is not a product. This includes variants that each have a distinct URL. Mark up product pages, not listing or category pages.
- Variants: follow the product variant documentation.
- Several currencies: one distinct URL per currency (for example one for CAD, one for USD).
- `Car` is not automatically a `Product` subtype. To attach ratings and be eligible, declare both types: `"@type": ["Product", "Car"]`.
- Pros and cons: only editorial product review pages qualify, not merchant product pages or customer reviews.
- Merchants optimizing for all shopping results: put `Product` markup in the initial HTML.
- JavaScript-generated `Product` markup makes Shopping crawls less frequent and less reliable, a problem for fast-changing price and availability. Ensure the server can handle increased Google crawl traffic.

### Content guidelines
- No content promoting widely prohibited or regulated goods, services or information that may facilitate serious, immediate or long-term harm: firearms and weapons, recreational drugs, tobacco and vaping, gambling-related products.

### `Product` properties
- Required: `name` (`Text`).
- Required: at least one of `review`, `aggregateRating`, `offers`. The Rich Results Test product-snippets section may warn if only `offers` is present without `review` or `aggregateRating`.
- Recommended `aggregateRating` (`AggregateRating`): follow the Review snippet guidelines.
- Recommended `offers` (`Offer` or `AggregateOffer`): use `Offer`, not `AggregateOffer`, to be eligible for the price drop enhancement.
- Recommended `review` (`Review`): follow the Review snippet guidelines. The reviewer name must be a valid `Person` or `Team` name (good: "James Smith", "CNET Reviewers"; bad: "50% off on Black Friday").
- To tell Google pros and cons manually, add `positiveNotes` and/or `negativeNotes` to the nested review.

### `Review` additions for pros and cons
- Availability: Dutch, English, French, German, Italian, Japanese, Polish, Portuguese, Spanish and Turkish, in all countries where Google Search is available.
- Google tries to detect pros and cons automatically; explicit markup overrides guesswork. Follow the pros and cons guidelines.
- Required: at least two statements in any combination of `positiveNotes` and `negativeNotes` (an `ItemList` with two positive statements is valid).
- Recommended: `positiveNotes`, `negativeNotes` (each an `ItemList`; multiple statements via `itemListElement` array of `ListItem`).

### `ItemList` for notes
- Required: `itemListElement` (`ListItem`, ordered), `itemListElement.name` (`Text`, the key statement).
- Recommended: `itemListElement.position` (`Integer`, 1 = first).

### `Offer` (snippet profile)
- Required: `price` or `priceSpecification.price` (`Number`; JSON string or number accepted). `0` is allowed for free products. If both `price` and `priceSpecification` encode the active price, `price` wins and `priceSpecification` is ignored. Complex pricing: see merchant listing page.
- Recommended `availability` (`ItemAvailability`): one value from `BackOrder`, `Discontinued`, `InStock`, `InStoreOnly`, `LimitedAvailability`, `OnlineOnly`, `OutOfStock`, `PreOrder`, `PreSale`, `SoldOut` (full `https://schema.org/` URL; short names also accepted).
- Recommended `priceCurrency` or `priceSpecification.priceCurrency` (`Text`, ISO 4217 three-letter): recommended for snippets so Google determines currency accurately, but required for merchant listings, so always provide it.
- Recommended `priceValidUntil` (`Date`, ISO 8601): the snippet may not display if the date is in the past.

### `UnitPriceSpecification`
- Required: `price` (`Number`).
- Recommended: `priceCurrency` (`Text`, ISO 4217); optional for snippets, required for merchant listings.

### `AggregateOffer`
- Describes one product sold by multiple merchants. Do not use it for a set of product variants.
- Required: `lowPrice` (`Number`, `.` as decimal separator, for example 1.23), `priceCurrency`.
- Recommended: `highPrice` (`Number`), `offerCount` (`Number`).

### Search Console
- Check after first deployment, after new templates or code changes, and periodically.
- First deployment: after indexing, use the relevant rich result status report. Expect valid items to rise with no rise in invalid ones. Fix invalid items, inspect the live URL, request validation.
- After template releases: an increase in invalid items means a broken template or interaction. A drop in valid items not matched by an increase in invalid items suggests markup is no longer embedded; use URL Inspection.
- Periodic: Performance report shows rich result impressions, clicks and average position (also via the Search Console API).
- Two reports: Merchant listings report (pages where shoppers can buy) and Product snippets report (reviews and aggregator pages). The Merchant listings report already checks product snippets that include `Offer`, so consult the Product snippets report only for non-merchant pages.

### Troubleshooting
- Ask your CMS provider for help; forward Search Console messages.
- Google does not guarantee display of rich results; see the General Structured Data Guidelines.
- Check the structured data errors list and the Unparsable structured data report.
- A structured data manual action causes the markup to be ignored (page still appears in Search). Use the Manual Actions report.
- Spammy content or spammy markup can be the cause even when the Rich Results Test passes; re-read the guidelines.
- Use the "Troubleshoot missing rich results / drop in total rich results" guide.
- Allow days for recrawl and reindex; ask in the Search Central forum if stuck.

## Merchant listing (`Product`, `Offer`)
https://developers.google.com/search/docs/appearance/structured-data/merchant-listing · Last updated: 2026-09-08

### Purpose and availability
- `Product` markup can make a page eligible for merchant listing experiences: shopping knowledge panel, Google Images, popular products and product snippets. They highlight price, availability, shipping and return information.
- For editorial review pages use the product snippet guide instead.
- Same implement/validate/deploy workflow as the product snippet page (JSON-LD, RDFa or Microdata).

### Examples (key lessons)
- Basic product page: `Product` with `name`, `image` (three aspect ratios), `description`, `sku`, `mpn`, `brand`, `review`, `aggregateRating`, `offers` (`Offer`).
- Shipping example: `Offer.shippingDetails` (`OfferShippingDetails`) with `shippingRate` (`MonetaryAmount`), `shippingDestination` (`DefinedRegion`), `deliveryTime` (`handlingTime` and `transitTime`). Example gives US shoppers a rate of 3.49 USD.
- Free shipping: `shippingRate.value` `"0"` for a destination such as US state NY (`addressRegion: ["NY"]`).
- Return details example: Swiss customers, return by mail within 60 days, return fee 3.49 CHF. Uses `returnPolicyCategory` finite window, `merchantReturnDays`, `returnMethod`, `returnFees` `ReturnShippingFees`, `returnShippingFeesAmount`.
- Certifications: CO2 class for a vehicle (`issuedBy` BMWK, `name` `Vehicle_CO2_Class`, `certificationRating`) and an EPREL energy label (`issuedBy` European_Commission, `name` `EPREL`, `certificationIdentification`).
- 3D model: `subjectOf` of type `3DModel` with `encoding.contentUrl` pointing to a glTF file.

### Pricing model
- Three price kinds:
  - Active price: the current price.
  - Strikethrough price: the higher regular price during a sale, may be shown struck through.
  - Member price: the price for members of a particular loyalty program.
- Encoding is via price specifications under `Offer` (the active price may also sit at `Offer` level with `price`/`priceCurrency`).
- `priceType` and `validForMemberTier` must never be combined. A price specification containing both is ignored.
  - Active price: neither property.
  - Strikethrough price: `priceType` = `https://schema.org/StrikethroughPrice` (`ListPrice` also allowed for a transition period), no `validForMemberTier`.
  - Member price: `validForMemberTier`, no `priceType`.
- Active price: either `price` + `priceCurrency` on the `Offer`, or `priceSpecification` (`UnitPriceSpecification`) with `price` + `priceCurrency`. If both, `Offer.price` wins.
- Sale pricing: the active price becomes a sale price when a second price spec with `priceType` `StrikethroughPrice` holds the original price. Never put `priceType` on the active price. Two forms: active price at `Offer` level plus one spec, or two `UnitPriceSpecification` objects in an array.
- Sale duration (ISO 8601, for example `2025-12-31T23:59:59+01:00`):
  - Start: `validFrom`. End: `validThrough` or `priceValidUntil`.
  - Provide both start and end. `validFrom` must be earlier than or equal to the end. Include time and timezone for accuracy.
  - Placement: on the `Offer` node when `Offer.price` is the sale price; on the `UnitPriceSpecification` that holds the sale price when using spec arrays. `priceValidUntil` does not apply to `PriceSpecification`.
- Member prices: the member spec holds `price`, `priceCurrency` and `validForMemberTier` (a `MemberProgramTier`, referenced by `@id` or by `name` + `isTierOf`). A regular price is still required. Several tiers may share a price via an array. Different prices need separate specs. One offer can combine sale price, strikethrough price and several tier prices.
- Member points: a spec with `membershipPointsEarned` plus `validForMemberTier` shows points instead of a price (see beta tag below).
- Unit pricing (important in EU, New Zealand, Australia for volume, length or weight): when unit pricing measure and base measure exist, put the active price inside a `UnitPriceSpecification` and use `referenceQuantity` (`QuantitativeValue` with `value`, `unitCode`, `valueReference`). Example: 200 ml priced at 200 EUR with a 100 ml base.

### Technical guidelines
- Only pages where the shopper can buy the product qualify; pages that merely link to other sellers do not. Google may try to verify merchant listing data before showing it.
- Only single-product pages (or several variants of one product, including variants with distinct URLs). Mark up product pages, not category or listing pages.
- Variants: follow the variant documentation.
- Several currencies: one distinct URL per currency.
- `Car`: co-type with `Product` (`["Product", "Car"]`) to attach ratings.
- Put `Product` markup in the initial HTML; JavaScript-generated markup makes Shopping crawls less frequent and less reliable (price and availability), and the server must cope with extra Google crawl load.
- Must also comply with: general structured data guidelines, Search Essentials, free listings guidelines.

### Content guidelines
- Same prohibition as snippets: no content promoting widely prohibited or regulated goods, services or information (firearms and weapons, recreational drugs, tobacco and vaping, gambling-related products).

### `Product` properties
- Required:
  - `name` (`Text`).
  - `image` (repeated `ImageObject` or `URL`): clearly show the product (white background preferred). Image URLs crawlable and indexable (check with URL Inspection). Images must represent the marked-up content and use a format Google Images supports. Best: several high-resolution images, at least 50K pixels (width × height), in 16x9, 4x3 and 1x1.
  - `offers` (`Offer`): merchant listings require `Offer`, not `AggregateOffer`, because the merchant must be the seller.
- Recommended:
  - `aggregateRating` (`AggregateRating`): follow Review snippet guidelines.
  - `audience` (`PeopleAudience` only).
  - `brand.name` (`Text`): at most one brand name.
  - `category` (`Text` or `CategoryCode`, array allowed, mixed):
    - Plain text = custom product type (like feed `product_type`); keep under 750 characters.
    - `CategoryCode` = Google Product Category (like `google_product_category`): `inCodeSet` is a Google Product Taxonomy URL, `codeValue` is the GPC ID (for example `2271`) or a full path using `>` as separator, each segment at least one letter.
  - `color` (`Text`; for example "yellow/sky blue").
  - `description` (`Text`): not mandatory but strongly recommended.
  - `gtin` | `gtin8` | `gtin12` | `gtin13` | `gtin14` | `isbn` (`Text`): include all applicable; prefer the most specific GTIN property; numeric form only, no URL form. `isbn` is valid only on `Book`: co-type `["Product", "Book"]`; ISBN-13 preferred.
  - `hasAdultConsideration` (`AdultOrientedEnumeration`): required in practice for adult-oriented products under Google's adult-oriented content policy. Only `https://schema.org/SexualContentConsideration` is supported. Such products may appear in Shopping ads and free listings but with age- and country-based restrictions.
  - `hasCertification` (`Certification`): up to 10; most relevant in Europe. Legacy `hasEnergyConsumptionDetails` (`EnergyConsumptionDetails` with `hasEnergyEfficiencyCategory`, `energyEfficiencyScaleMin`, `energyEfficiencyScaleMax`) is still supported; `hasCertification` preferred.
  - `inProductGroupWithID` (`Text`): at most one value; the parent group ID.
  - `isVariantOf` (`ProductGroup`).
  - `material` (`Text`; for example "Cotton/Polyester").
  - `mpn` (`Text`): manufacturer part number.
  - `pattern` (`Text`).
  - `review` (`Review`): reviewer name must be a valid `Person` or `Team` name.
  - `size` (`Text` or `SizeSpecification`): at most one value.
  - `sku` (`Text`): merchant-specific ID, at most one value. Unicode valid for interchange, no whitespace characters (Unicode whitespace property), ASCII-only recommended.
  - `subjectOf` (`3DModel`): at most one.

### `3DModel`
- Required: `encoding` (`MediaObject`), `encoding.contentUrl` (`URL` to a glTF file with `.gltf` or `.glb` suffix). Only glTF is supported.

### `Offer` properties
- Required:
  - `price` or `priceSpecification.price` (`Number`): the current active price. Merchant listings require a price greater than zero (unlike snippets, which allow 0).
  - `priceCurrency` or `priceSpecification.priceCurrency` (`Text`, ISO 4217): required whenever a price is given.
  - `priceSpecification` (`UnitPriceSpecification`): alternative active-price location and carrier of complex prices. `Offer.price` wins over a duplicate.
- Recommended:
  - `availability` (`ItemAvailability`): one value only. Same ten values as snippets.
  - `hasMerchantReturnPolicy` (`MerchantReturnPolicy`): provide a global policy under `Organization` instead. Use this at offer level only to override it or when no standard policy exists. Offer-level supports a subset of properties. To reference a global policy from another page, use only `@id` (`{"@id": "https://example.com/returns#policy"}`).
  - `itemCondition` (`OfferItemCondition`): one of `NewCondition`, `RefurbishedCondition`, `UsedCondition`; one value only.
  - `priceValidUntil` (`Date`, ISO 8601): the listing may not display if the date is in the past.
  - `shippingDetails` (`OfferShippingDetails`): same global-vs-override logic as returns. To reference a global shipping policy, use `OfferShippingDetails` containing only `hasShippingService` with an `@id`.
  - `url` (`URL`): page where the product can be bought; may be the preferred URL with variant options preselected; may be omitted; never multiple URLs.
  - `validFrom`, `validThrough` (`DateTime` or `Date`, ISO 8601).

### `UnitPriceSpecification`
- Required: `price` (`Number`), `priceCurrency` (`Text`).
- Recommended:
  - `membershipPointsEarned` (`Number`, whole number of points) (beta): use only with `validForMemberTier`. May not affect Search right away.
  - `priceType` (`PriceTypeEnumeration`): only `https://schema.org/StrikethroughPrice` supported; use only to show sale pricing; a current price must also exist on the `Offer`.
  - `referenceQuantity` (`QuantitativeValue` for unit pricing).
  - `validForMemberTier` (`MemberProgramTier`): multiple tiers allowed when the price is identical; a regular price must also exist. Tiers are defined in Merchant Center or via `MemberProgram` markup on a separate Organization page. Referenced by `name` + `isTierOf` (Merchant Center-defined) or by `@id` URI (markup-defined). (beta) Off-page `MemberProgramTier` markup might not show right away.
  - `validFrom`, `validThrough`.
- If both `priceType` and `validForMemberTier` are used, the spec is ignored.

### `QuantitativeValue` (unit pricing)
- Required: `unitCode` (`Text` or `URL`): UN/CEFACT codes or the human-readable equivalents from Merchant Center's unit pricing measure list, except `sheet` and `item` (feed-only). `value` (`Text`, numeric value of the unit sold).
- Recommended: `valueReference` (`QuantitativeValue`, the base quantity).

### `SizeSpecification` (all recommended)
- `name` (`Text`, for example "XL").
- `sizeGroup` (`WearableSizeGroupEnumeration` or `Text`): at most two. Values: `WearableSizeGroupRegular`, `Petite`, `Plus`, `Tall`, `Big`, `Maternity` (short names accepted). Google also understands the text `size_type` values, but other search engines may not; schema.org enums recommended.
- `sizeSystem` (`WearableSizeSystemEnumeration` or `Text`): `AU`, `BR`, `CN`, `DE`, `Europe`, `FR`, `IT`, `JP`, `MX`, `UK`, `US` (as `WearableSizeSystemXX`; short names accepted). Text `size_system` values understood by Google but schema.org enums recommended.

### `PeopleAudience` (all recommended)
- `suggestedGender` (`Text` or `GenderType`): `https://schema.org/Male`, `https://schema.org/Female`, or `Unisex` (case-insensitive, no schema.org prefix). Raw `male`/`female` accepted.
- `suggestedMaxAge` (or `suggestedAge.maxValue`) in years, mapped by Google to `0.25` (newborns), `1.0` (infants), `5.0` (toddlers), `13.0` (kids). Omit for adults.
- `suggestedMinAge` (or `suggestedAge.minValue`): mapped to `0` (newborns), `0.25` (infants), `1.0` (toddlers), `5.0` (kids), `13.0` (adults).

### `Certification`
- Required: `issuedBy` (`Organization`, by `name`): `EC` or `European_Commission` (EU energy labels), `ADEME` (French vehicle CO2 classes), `BMWK` (German vehicle CO2 classes). Required: `name`: `EPREL` (EU energy efficiency, EPREL database), `Vehicle_CO2_Class`, `Vehicle_CO2_Class_Discharged_Battery`.
- Recommended: `certificationIdentification` (`Text`, the code, for example EPREL `123456`): required for European energy labels. Merchants serving NO, CH or the UK without EPREL codes can use `certificationRating` instead.
- Recommended: `certificationRating` (`Rating`): ignored when `certificationIdentification` is present. Holds CO2 class or energy rating when no EPREL code. Nested `ratingValue` (required when used), `bestRating`, `worstRating` (the last two also required for EU energy efficiency ratings).

### `OfferShippingDetails` (not required, but these are required for the shipping enhancement)
- Use multiple `shippingDetails` for multiple options (for example express, standard), each with its own `shippingRate`/`deliveryTime`.
- Required: `deliveryTime` (`ShippingDeliveryTime`; at most one; contains `handlingTime`, `transitTime`); `shippingDestination` (`DefinedRegion`, with `addressCountry`); `shippingRate` (`MonetaryAmount`; one per `OfferShippingDetails`); `shippingRate.currency` (ISO 4217; must equal the offer currency); `shippingRate.value` or `shippingRate.maxValue` (`Number`; string values without currency symbols, thousands separators or spaces; `0` = free shipping).
- At least one of `shippingRate.value` or `shippingRate.maxValue` is required, together with `currency`.

### `DefinedRegion` (offer level)
- Required: `addressCountry` (ISO 3166-1 alpha-2).
- Recommended: choose either `addressRegion` or `postalCode` (never both; do not mix region-spec ways in one instance); omitted = whole country.
  - `addressRegion`: ISO 3166-2 subdivision code without country prefix, 2 or 3 characters. (region: US, Australia, Japan only; examples `NY`, `NSW`, `03`).
  - `postalCode`: (region: Australia, Canada, US only; for example `94043`).
- Custom regions are currently supported only for a restricted set of countries (see Merchant Center regions help).

### `ShippingDeliveryTime` and shipping `QuantitativeValue`
- Recommended on `ShippingDeliveryTime`: `handlingTime` (order receipt to leaving warehouse), `transitTime` (sent to arrival).
- Each `QuantitativeValue`: `minValue`, `maxValue` (non-negative whole numbers, days) and `unitCode` (`DAY` or `d`) all required.

### `MerchantReturnPolicy` (offer level)
- Product-level policy wins over organization-level when both exist.
- Required: `applicableCountry` (up to 50 ISO 3166-1 alpha-2 codes); `returnPolicyCategory`: `MerchantReturnFiniteReturnWindow` (needs `merchantReturnDays`), `MerchantReturnNotPermitted`, `MerchantReturnUnlimitedWindow`.
- Recommended:
  - `merchantReturnDays` (`Integer`, days from delivery; required for finite window).
  - `returnFees`: `FreeReturn` (no `returnShippingFeesAmount`), `ReturnFeesCustomerResponsibility` (no amount), `ReturnShippingFees` (non-zero `returnShippingFeesAmount` required).
  - `returnMethod`: `ReturnAtKiosk`, `ReturnByMail`, `ReturnInStore` (multiple allowed; recommended only for finite or unlimited windows).
  - `returnShippingFeesAmount` (`MonetaryAmount`; only for non-zero fees).

### Alternative: configure shipping and returns outside markup
- If markup is hard to keep current and you have a Merchant Center account, configure shipping and return policies in Merchant Center, or account-level policies in Search Console (auto-added to Merchant Center).
- Precedence when defined in several places (strongest to weakest): product-level feeds in Merchant Center; Content API for Shopping settings; Merchant Center or Search Console settings; product-level merchant listing markup; Organization-level markup.

### Search Console and troubleshooting
- Same monitoring guidance as the product snippet page: rich result status reports, Performance report. Merchant listings report for purchasable pages; Product snippets report for reviews and aggregators.
- Same troubleshooting list as above.

## Variants (`ProductGroup`, `Product`)
https://developers.google.com/search/docs/appearance/structured-data/product-variants · Last updated: 2026-09-08

### Purpose
- Variants are different sizes, colors, materials or patterns of one parent product (apparel, shoes, furniture, electronics, luggage).
- `ProductGroup` plus `variesBy`, `hasVariant`, `productGroupID` groups variants, in addition to `Product` markup. It also makes products eligible for variant display in merchant listing experiences.
- `ProductGroup` can hold common properties (brand, reviews) and variant-determining properties, reducing duplication.
- Same implement/validate/deploy workflow as other product pages.

### Site design approaches and examples
- Single-page site: all variants are selectable on one page without reload, usually via query parameters. Base URL shows no preselected variant; each variant has its own preselecting URL (for example `?size=small&color=green`). Page content (image, price, availability) changes dynamically but markup does not.
  - Nested approach (recommended; most compact): variants nested under `ProductGroup` via `hasVariant`. Common title, description, brand, pattern, material and audience on the group. Variant-specific names and descriptions on each `Product`. `variesBy` lists the varying properties. `productGroupID` is the parent SKU (no need to repeat `inProductGroupWithID`). `ProductGroup` and each `Offer` carry distinct URLs (URLs may alternatively sit on `Product`). Shared `OfferShippingDetails` and `MerchantReturnPolicy` nodes are referenced by `@id`.
  - Separate approach: variants defined as top-level `Product` nodes pointing to the group via `isVariantOf` with `@id`. May be easier for some CMSes.
- Multi-page site: variants spread over pages (for example one page per color), with page reload to switch.
  - The full `ProductGroup` definition must be repeated on every variant page (there is no off-page reference, because the group needs the common attributes).
  - `ProductGroup` has no canonical URL, because no single URL represents it, so omit `url` on it.
  - Each page fully defines its own variants, plus a bare variant containing only `url` to point to variants on the other pages, which helps Google find them.
  - Nested and separate approaches both work.

### Technical guidelines
- Every variant needs a unique ID in its markup (`sku` or `gtin`).
- Every product group needs a unique ID: `productGroupID` on the group or `inProductGroupWithID` on variants.
- Also provide `Product` markup with the required properties for merchant listings (or product snippets).
- Single-page sites: exactly one canonical URL for the whole `ProductGroup`, typically the base URL without a preselected variant. Not applicable to multi-page sites.
- Multi-page sites: each page's markup must be full and self-contained; off-page entities must not be needed to understand it.
- Each variant must be preselectable through a distinct URL (query parameters) so Google can crawl and identify it. That includes the right image, price, availability and the ability to add the variant to the cart.
- Prefer `Product` markup in the initial HTML; JavaScript-generated markup makes Shopping crawls less frequent and reliable, and the server needs capacity for the extra crawl load.
- Must also comply with general structured data guidelines, Search Essentials and free listings guidelines.

### `ProductGroup` properties
- Required: `name` (`Text`). Variant `Product` names must be more specific (for example "Wool winter coat - green, size small").
- Recommended:
  - `aggregateRating` (`AggregateRating`): representative of all variants.
  - `brand` (`Brand`) and `brand.name` (`Text`): same for all variants; no need to repeat on `Product` if on the group.
  - `description` (`Text` or `TextObject`): variant descriptions should be more specific (color, size, material); also add a description per variant.
  - `hasAdultConsideration` (`AdultOrientedEnumeration`): same rule as on `Product` (only `https://schema.org/SexualContentConsideration` supported).
  - `hasVariant` (`Product`): typically several. Alternative is `isVariantOf` on each variant.
  - `productGroupID` (`Text`, the parent SKU): give it on the group or via `inProductGroupWithID` on variants. If both are given, they must match.
  - `review` (`Review`).
  - `url` (`URL`): single-page sites only; the URL without variant selectors. Do not use on multi-page sites.
  - `variesBy` (`DefinedTerm`): full schema.org URLs. Supported: `https://schema.org/color`, `size`, `suggestedAge`, `suggestedGender`, `material`, `pattern`.

### Troubleshooting
- Same list as the other pages: CMS help, no guarantee of display, error and Unparsable reports, Manual Actions, re-read guidelines, missing rich results guide, wait for recrawl, forum.

## Loyalty program (`MemberProgram`)
https://developers.google.com/search/docs/appearance/structured-data/loyalty-program · Last updated: 2026-09-08

### Purpose and availability
- Lets Google show loyalty benefits (member prices, points) with products and knowledge panels.
- Programs are declared with `MemberProgram` nested under `Organization` (property `hasMemberProgram`; example uses `OnlineStore`). Per-product benefits are separate: `UnitPriceSpecification` under `Offer` (see merchant listing).
- (region: Australia, Brazil, Canada, France, Germany, Mexico, UK, US) desktop and mobile.
- Same implement/validate/deploy workflow.

### Guidelines
- Nest `MemberProgram` under `Organization` on the page that holds your business's administrative details and policies.
- `MemberProgram` works together with `validForMemberTier` and `membershipPointsEarned` on product price specifications.
- Also comply with general structured data guidelines and Search Essentials.
- Alternative: configure the program in Merchant Center. If both markup and Merchant Center define programs, Google uses the Merchant Center settings.

### Example lesson
- Two-tier program: tiers carry `@id` fragments (referenced later by `validForMemberTier`), `hasTierBenefit` array, optional `hasTierRequirement` (for example a credit card for the gold tier) and `membershipPointsEarned`.

### `MemberProgram`
- Required: `description` (`Text`, main benefits), `hasTiers` (repeated `MemberProgramTier`; at least one), `name` (`Text`).
- Recommended: `url` (`URL`, sign-up page; one only; if omitted, the page containing the markup is assumed).

### `MemberProgramTier`
- Required:
  - `hasTierBenefit` (repeated `TierBenefitEnumeration`): `https://schema.org/TierBenefitLoyaltyPoints` (also specify `membershipPointsEarned`), `https://schema.org/TierBenefitLoyaltyPrice` (member-only price). Short names accepted.
  - `name` (`Text`).
- Recommended:
  - `hasTierRequirement` (`CreditCard`, `MonetaryAmount`, `UnitPriceSpecification` or `Text`): if omitted, anyone can join free. `CreditCard`: card name. `MonetaryAmount`: minimum spend (`value`, `currency`). `UnitPriceSpecification`: periodic fee (`price`, `priceCurrency`, `billingDuration`, `billingIncrement`, `unitCode` such as `MON`). `Text`: any other requirement.
  - `membershipPointsEarned` (`QuantitativeValue`): points per currency unit spent, when the benefit is loyalty points.
  - `url` (`URL`): sign-up page for this tier; one only.
> Note: `membershipPointsEarned` is a `QuantitativeValue` per currency unit on the tier here, but a whole `Number` earned for a purchase on a price specification in the merchant listing page (marked beta there). The two use different semantics.

### Troubleshooting
- Same list as above.

## Merchant return policy (`MerchantReturnPolicy`)
https://developers.google.com/search/docs/appearance/structured-data/return-policy · Last updated: 2026-09-08

### Purpose
- Google can show return policies next to products and in knowledge panels. Supports a link to the policy page or detailed conditions: return conditions, methods, fees, refund options.
- Standard policy for most or all products: `MerchantReturnPolicy` under `Organization` via `hasMerchantReturnPolicy`.
- Per-product override: one or more `MerchantReturnPolicy` under `Offer`, supporting fewer properties (see merchant listing).
- Same implement/validate/deploy workflow.

### Examples (key lessons)
- Online store with return policy for DE, AT, CH, returns by mail to Ireland (`returnPolicyCountry` `IE`): 60-day finite window, `itemCondition` new only, `FreeReturn`, `FullRefund`, `ReturnLabelCustomerResponsibility`. Shows it nested in an `OnlineStore` with other organization properties.
- Complex example: several accepted conditions (new and damaged), `ReturnShippingFees` with `returnShippingFeesAmount`, `returnLabelSource`, separate settings for customer remorse (own fees, amount, label source) and for item defects (free, label in box), plus a `returnPolicySeasonalOverride` limiting the window to 30 days.
> Note: the seasonal-override sample has `endDate` "2025-01-05" before `startDate` "2025-12-01"; treat as a sample typo (an end date must follow the start date).

### Guidelines
- Put return information on one page describing the business's policy; not needed on every page. Include `MerchantReturnPolicy` under `Organization` there.
- Non-standard product: `MerchantReturnPolicy` directly under `Offer` (subset of properties).
- Also comply with general structured data guidelines and Search Essentials.

### `MerchantReturnPolicy` (under `Organization`)
- Required: choose Option A or Option B.
  - Option A: `applicableCountry` (`Text`; where the product is sold and returned from; ISO 3166-1 alpha-2; up to 50) plus `returnPolicyCategory` (`MerchantReturnFiniteReturnWindow` which requires `merchantReturnDays`, `MerchantReturnNotPermitted`, `MerchantReturnUnlimitedWindow`).
  - Option B: `merchantReturnLink` (`URL` of a page describing the policy; can be your own or a third-party returns service).
- Recommended when category is finite or unlimited:
  - `merchantReturnDays` (`Integer`, days from delivery; required for finite window).
  - `returnFees` (default type): `FreeReturn`, `ReturnFeesCustomerResponsibility` (neither may carry `returnShippingFeesAmount`), `ReturnShippingFees` (needs non-zero amount).
  - `returnMethod`: `ReturnAtKiosk`, `ReturnByMail`, `ReturnInStore` (one or more).
  - `returnShippingFeesAmount` (`MonetaryAmount`): only when `returnFees` = `ReturnShippingFees`.
- Additionally recommended (finite or unlimited windows):
  - `customerRemorseReturnFees`, `customerRemorseReturnLabelSource`, `customerRemorseReturnShippingFeesAmount`: fee, label source and amount for remorse returns (amount only if non-zero).
  - `itemCondition` (`OfferItemCondition`; multiple allowed): `DamagedCondition`, `NewCondition`, `RefurbishedCondition`, `UsedCondition`.
  - `itemDefectReturnFees`, `itemDefectReturnLabelSource`, `itemDefectReturnShippingFeesAmount`: same for defects.
  - `refundType` (`RefundType`): `ExchangeRefund`, `FullRefund`, `StoreCreditRefund`.
  - `restockingFee` (`MonetaryAmount` or `Number`): `Number` charges a percentage of the price paid; `MonetaryAmount` a fixed amount.
  - `returnLabelSource` (`ReturnLabelSourceEnumeration`): `ReturnLabelCustomerResponsibility`, `ReturnLabelDownloadAndPrint`, `ReturnLabelInBox`.
  - `returnPolicyCountry` (`Text`): country where returns are sent; may differ from the delivery country; up to 50.

### Seasonal overrides (organization level)
- Required: `returnPolicySeasonalOverride` (`MerchantReturnPolicySeasonalOverride`; an array for several periods) and `returnPolicySeasonalOverride.returnPolicyCategory` (same three values; finite window requires `merchantReturnDays`).
- Recommended: `startDate`, `endDate` (`Date` or `DateTime`), `merchantReturnDays` (`Integer`, required if category is finite window).
> Note: the page types `returnPolicySeasonalOverride.merchantReturnDays` as `Integer` or `Date` or `DateTime`; use an integer day count as the other definition describes.

### Alternative and precedence
- Configure returns in Merchant Center or account-level in Search Console (auto-added to Merchant Center) if markup is hard to maintain.
- Precedence (strongest to weakest): Content API for Shopping return settings; Merchant Center or Search Console settings; product-level merchant listing markup; Organization-level markup. If markup and Search Console both exist, only Search Console is used.
> Note: the merchant listing page's combined precedence list adds product-level Merchant Center feeds as the strongest source; the return policy page omits it. The merchant listing list is the superset.

### Troubleshooting
- Same list as above.

## Merchant shipping policy (`ShippingService`)
https://developers.google.com/search/docs/appearance/structured-data/shipping-policy · Last updated: 2026-09-08

### Purpose
- Google can show shipping info next to products and in knowledge panels. `ShippingService` expresses cost and delivery time by product weight, dimensions, order value or location.
- Standard policy: `ShippingService` under `Organization` via `hasShippingService`.
- Per-product override: `OfferShippingDetails` under `Offer.shippingDetails` (fewer properties; see merchant listing).
- Same implement/validate/deploy workflow.

### Example lesson
- One `ShippingService` holds a `handlingTime` (`ServicePeriod` with `cutoffTime`, `duration`, `businessDays`) and several `shippingConditions`:
  - US and CA by order value bands: cheaper tier with rate, higher tier free.
  - MX: `doesNotShip: true` below a threshold; above it `ShippingRateSettings` with `orderPercentage` 0.10.
- Order value bands use `orderValue` `MonetaryAmount` with `minValue`/`maxValue`/`currency`.
> Note: the example text describes "free 2-day" and "4-day" Mexico shipping, while the markup uses transit durations that do not exactly match (and `maxValue` 29.99 vs `minValue` 30). Treat as illustrative.

### Guidelines
- Describe the shipping policy on one page of your site; no need to repeat it on every page. Place `ShippingService` under `Organization` there.
- Non-standard product: `OfferShippingDetails` directly under `Offer`.
- Also comply with general structured data guidelines and Search Essentials.

### `ShippingService` (under `Organization`)
- Required: `shippingConditions` (`ShippingConditions`; several allowed). When several conditions match a product, Google uses the lowest shipping cost; at equal cost, the fastest speed.
- Recommended:
  - `name` (`Text`, unique name, for example "Standard Shipping").
  - `description` (`Text`).
  - `fulfillmentType`: `FulfillmentTypeDelivery` (default; to customer address) or `FulfillmentTypeCollectionPoint` (customer pickup).
  - `handlingTime` (`ServicePeriod`).
  - `validForMemberTier` (`MemberProgramTier`): multiple tiers allowed if identical settings. If used for member shipping benefits, at least one regular (non-member) shipping service must also exist. Referenced by `name` + `isTierOf` (Merchant Center) or by `@id` (markup on a separate organization page). (beta) off-page `MemberProgramTier` markup may not show right away.

### `ServicePeriod` for handling times
- Also used for transit times; `cutoffTime` is not used for transit.
- Recommended: `businessDays` (`DayOfWeek`; days orders are processed), `cutoffTime` (`Time`, ISO 8601 with offset, for example `22:30:00-05:00`; orders after the cutoff add one day to the delivery estimate), `duration` (`QuantitativeValue`; delay from order to leaving warehouse; `0` means same-day processing before cutoff).
> Note: the page says `23:30:00-05:00` represents 6:30 pm EST. That conversion is inconsistent with the offset; 23:30 at UTC-5 is 11:30 pm local time.

### `QuantitativeValue` (handling and transit times)
- Provide either `value` (fixed) or `maxValue` (upper bound) together with `unitCode`; `minValue` is optional (lower bound).
- `value`, `minValue`, `maxValue`: non-negative whole numbers (days). If `value` is given, omit `minValue` and `maxValue`. `unitCode`: `DAY` or `d`.

### `ShippingConditions` (all recommended)
- With no shipping destination, conditions apply to all destinations worldwide.
- `doesNotShip` (`Boolean`): `true` when shipping origin to destination is unavailable for the given `weight`, `numItems`, `orderValue` combination.
- `numItems` (`QuantitativeValue`), `orderValue` (`MonetaryAmount`), `weight` (`QuantitativeValue`): ranges for which the condition applies.
- `shippingDestination`, `shippingOrigin` (`DefinedRegion`).
- `seasonalOverride` (`OpeningHoursSpecification`): limited validity period.
- `shippingRate` (`ShippingRateSettings` or `MonetaryAmount`): only when `doesNotShip` is absent or `false`.
- `transitTime` (`ServicePeriod`): only when `doesNotShip` is absent or `false`.

### `DefinedRegion`
- Required: `addressCountry` (ISO 3166-1 alpha-2).
- Recommended: `addressRegion` (ISO 3166-2 subdivision, 2 or 3 characters, no country prefix; (region: US, Australia, Japan only); examples `NY`, `NSW`, `03`); `postalCode` ((region: Australia, Canada, US) for example `94043`). Never both region and postal code.

### `ServicePeriod` for transit times
- Recommended: `businessDays` (`DayOfWeek`; if the business works Monday to Saturday it can be omitted), `duration` (`QuantitativeValue`, business days in transit).

### Packing-dimension `QuantitativeValue` (`weight`, `numItems`)
- Provide `minValue` or `maxValue` (at least one). `minValue` defaults to 0 and must be less than `maxValue`; `maxValue` defaults to infinity.
- `unitCode`: UN/CEFACT three-character code. Weight: `LBR` (pound) or `KGM` (kilogram). Number of items: omit, or use `H87`.

### `MonetaryAmount` for order value
- Required: `currency` (ISO 4217), `minValue`, `maxValue`. Either `minValue` or `maxValue` must be provided; `minValue` defaults to 0, `maxValue` to infinity.

### `MonetaryAmount` for shipping rate
- Required: `currency` (ISO 4217) and either `value` (fixed; `0` = free) or `maxValue` (maximum cost; then omit `value`).
- A simpler alternative to `ShippingRateSettings`.

### `ShippingRateSettings`
- Rate as a fraction of order value or goods weight. Provide `orderPercentage` or `weightPercentage` (each `Number` between `0` and `1`).

### `OpeningHoursSpecification` for seasonal overrides
- Provide at least one of `validFrom`, `validThrough` (`Date`, ISO 8601: first and last valid date).

### Alternative and precedence
- Configure delivery settings in Merchant Center, or account-level shipping policies in Search Console (auto-added to Merchant Center). If markup and Search Console both exist, only Search Console is used.
- Precedence (strongest to weakest): Content API for Shopping (account-level shipping settings); Merchant Center or Search Console settings; product-level merchant listing markup; Organization-level markup.
> Note: the merchant listing page lists product-level Merchant Center feeds above these (strongest); this page omits that tier.

### Troubleshooting
- Same list as above.
