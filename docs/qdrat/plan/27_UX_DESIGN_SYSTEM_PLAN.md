# One product experience

Owner: frontend/ shared shell and design system. Navigation: Home, My Work, Inbox, Search, suites visible by permission, and Settings. Command palette and Ask Qdrat are optional entry points into the same authorized actions. Do → Understand → Design is progressive disclosure: perform a task, inspect its history/meaning, then configure it if permitted.

ObjectPage uses stable identity/title, status/owner, primary actions, permitted fields, related objects and activity/evidence timeline. Shared views: table, board, timeline/Gantt, calendar, tree, graph, map, dashboard and form. Every graphic view has an accessible list/table equivalent. Bulk actions preview exact targets and partial errors.

Design tokens cover spacing, type, contrast, focus, motion, density, status and semantic colors. Use CSS logical properties, direction-aware icons only where semantic, bidi isolation for IDs/emails/numbers, and original text preservation. Arabic is a first-class authored locale; machine translation is a draft. Names, dates, currencies and calendars format with pinned locale assets. Avoid assuming name order, Western digits or weekend.

Target [WCAG 2.2 AA](https://www.w3.org/TR/WCAG22/). Automated axe checks supplement manual keyboard/screen-reader, zoom/reflow, target-size and Arabic reading-order tests. CLDR main was marked prerelease at research time; qualify a stable locale release for distribution.

Use the [W3C Arabic and Persian layout requirements](https://www.w3.org/TR/alreq/) as an informative layout reference, explicitly a draft note rather than a compliance standard. Test joining/shaping, diacritics, mixed-direction identifiers and number/date presentation in browser and generated documents with the actual bundled fonts.

Offline means the customer deployment can operate without internet. Disconnected client editing is a separate limited capability: permitted cached reference data and unsent drafts only, visible sync status and reauthentication before submission. Payroll release, permission changes and approvals require the authoritative server online. Never pretend a queued action has succeeded.

Admin journeys are product requirements: first install, bootstrap owner/MFA, restore keys, map source fields, repair failed sync, review an approval, resolve unknown external outcome, rotate secrets, install extension, inspect egress, backup/restore and upgrade. Error copy states what happened, whether an effect may have occurred and the safe next action. Routine users do not see workflow engine/provider implementation details.
