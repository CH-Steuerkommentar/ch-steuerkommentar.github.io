// Website des Kommentars (Astro + Starlight).
// SITE und BASE setzt der GitHub-Workflow; lokal gelten die Standardwerte.
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';


// Externe Links in allen Markdown-Seiten bereits beim Bau mit target="_blank" versehen.
function externeLinksNeuerTab() {
  const besuchen = (knoten) => {
    if (knoten.type === 'element' && knoten.tagName === 'a') {
      const href = String(knoten.properties?.href ?? '');
      if (/^https?:\/\//.test(href)) {
        knoten.properties.target = '_blank';
        knoten.properties.rel = ['noopener'];
      }
    }
    (knoten.children ?? []).forEach(besuchen);
  };
  return (baum) => besuchen(baum);
}

const WERK = process.env.WERK_NAME ?? 'ILE-HSG Steuerrechtskommentar';

export default defineConfig({
  site: process.env.SITE ?? 'https://example.github.io',
  base: process.env.BASE ?? '/',
  trailingSlash: 'always',
  markdown: {
    rehypePlugins: [externeLinksNeuerTab],
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
      components: {
        ThemeSelect: './src/components/Leer.astro',
        ThemeProvider: './src/components/NurHell.astro',
        Footer: './src/components/Fusszeile.astro',
        Sidebar: './src/components/Seitenleiste.astro',
        SiteTitle: './src/components/Seitentitel.astro',
      },
      head: [
        { tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.googleapis.com' } },
        { tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' } },
        { tag: 'link', attrs: { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Cabin:wght@400;500;600&display=swap' } },
        { tag: 'link', attrs: { rel: 'preload', as: 'font', type: 'font/woff2', crossorigin: '', href: 'https://ile.unisg.ch/typo3conf/ext/cs2_prototypes/src/dist/fonts/GillSansMTPro-Light.woff2' } },
      ],
      lastUpdated: true,
      pagination: false,
      tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
      sidebar: [
        { label: 'DBG', collapsed: true, items: [{ autogenerate: { directory: 'dbg' } }] },
        { label: 'StHG', collapsed: true, items: [{ autogenerate: { directory: 'sthg' } }] },
        { label: 'VStG', collapsed: true, items: [{ autogenerate: { directory: 'vstg' } }] },
        { label: 'MWSTG', collapsed: true, items: [{ autogenerate: { directory: 'mwstg' } }] },
        { label: 'StG', collapsed: true, items: [{ autogenerate: { directory: 'stg' } }] },
        { label: 'Über den ILE-HSG Steuerrechtskommentar', link: '/ueber/' },
      ],
    }),
  ],
});
