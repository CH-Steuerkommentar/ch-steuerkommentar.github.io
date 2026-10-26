// Website des Kommentars (Astro + Starlight).
// SITE und BASE setzt der GitHub-Workflow; lokal gelten die Standardwerte.
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

const WERK = process.env.WERK_NAME ?? 'Offener Steuerrechtskommentar';

export default defineConfig({
  site: process.env.SITE ?? 'https://example.github.io',
  base: process.env.BASE ?? '/',
  trailingSlash: 'always',
  markdown: {
    remarkRehype: {
      footnoteLabel: 'Fussnoten',
      footnoteBackLabel: 'Zurück zum Text',
    },
  },
  integrations: [
    starlight({
      title: WERK,
      defaultLocale: 'root',
      locales: { root: { label: 'Deutsch', lang: 'de-CH' } },
      description: 'Offener Online-Kommentar zum Steuerrecht des Bundes',
      customCss: ['./src/styles/kommentar.css'],
      lastUpdated: true,
      pagination: false,
      tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
      editLink: process.env.EDIT_LINK ? { baseUrl: process.env.EDIT_LINK } : undefined,
      sidebar: [
        { label: 'DBG', collapsed: true, items: [{ autogenerate: { directory: 'dbg' } }] },
        { label: 'StHG', collapsed: true, items: [{ autogenerate: { directory: 'sthg' } }] },
        { label: 'VStG', collapsed: true, items: [{ autogenerate: { directory: 'vstg' } }] },
        { label: 'MWSTG', collapsed: true, items: [{ autogenerate: { directory: 'mwstg' } }] },
        { label: 'StG', collapsed: true, items: [{ autogenerate: { directory: 'stg' } }] },
        { label: 'Über dieses Werk', link: '/ueber/' },
      ],
    }),
  ],
});
