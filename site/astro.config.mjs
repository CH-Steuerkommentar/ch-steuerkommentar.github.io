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

// Französische Seiten: Überschrift der Fussnoten auf Französisch.
function fussnotenFranzoesisch() {
  return (baum, datei) => {
    const pfad = String(datei?.path ?? datei?.history?.[0] ?? '').replace(/\\/g, '/');
    if (!pfad.includes('/content/docs/fr/')) return;
    const suchen = (k) => {
      if (k.type === 'element' && k.properties?.id === 'footnote-label') {
        k.children = [{ type: 'text', value: 'Notes' }];
      }
      if (k.type === 'element' && k.tagName === 'a' && k.properties?.ariaLabel === 'Zurück zum Text') {
        k.properties.ariaLabel = 'Retour au texte';
      }
      (k.children ?? []).forEach(suchen);
    };
    suchen(baum);
  };
}

const OG_BILD = (process.env.SITE ?? 'https://example.github.io') + (process.env.BASE ?? '/') + 'og.png';
const WERK = process.env.WERK_NAME ?? 'ILE-HSG Steuerrechtskommentar';

export default defineConfig({
  site: process.env.SITE ?? 'https://example.github.io',
  base: process.env.BASE ?? '/',
  trailingSlash: 'always',
  markdown: {
    rehypePlugins: [externeLinksNeuerTab, fussnotenFranzoesisch],
    remarkRehype: {
      footnoteLabel: 'Fussnoten',
      footnoteBackLabel: 'Zurück zum Text',
    },
  },
  integrations: [
    starlight({
      title: { 'de-CH': WERK, fr: 'Commentaire de droit fiscal ILE-HSG' },
      defaultLocale: 'root',
      locales: { root: { label: 'Deutsch', lang: 'de-CH' }, fr: { label: 'Français', lang: 'fr' } },
      description: 'Offener Online-Kommentar zum Steuerrecht des Bundes',
      customCss: ['./src/styles/kommentar.css'],
      components: {
        ThemeSelect: './src/components/Leer.astro',
        ThemeProvider: './src/components/NurHell.astro',
        Footer: './src/components/Fusszeile.astro',
        Sidebar: './src/components/Seitenleiste.astro',
        SiteTitle: './src/components/Seitentitel.astro',
        LanguageSelect: './src/components/Sprachwahl.astro',
        MobileMenuFooter: './src/components/Leer.astro',
      },
      favicon: '/favicon-32.png',
      head: [
        { tag: 'meta', attrs: { property: 'og:image', content: OG_BILD } },
        { tag: 'meta', attrs: { name: 'twitter:card', content: 'summary_large_image' } },
        { tag: 'link', attrs: { rel: 'apple-touch-icon', href: '/apple-touch-icon.png' } },
        { tag: 'link', attrs: { rel: 'icon', type: 'image/png', sizes: '512x512', href: '/favicon-512.png' } },
        { tag: 'link', attrs: { rel: 'preload', as: 'font', type: 'font/woff2', crossorigin: '', href: 'https://ile.unisg.ch/typo3conf/ext/cs2_prototypes/src/dist/fonts/GillSansMTPro-Light.woff2' } },
      ],
      lastUpdated: true,
      pagination: true,
      tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
      sidebar: [
        { label: 'DBG', translations: { fr: 'LIFD' }, collapsed: true, items: [{ autogenerate: { directory: 'dbg' } }] },
        { label: 'StHG', translations: { fr: 'LHID' }, collapsed: true, items: [{ autogenerate: { directory: 'sthg' } }] },
        { label: 'VStG', translations: { fr: 'LIA' }, collapsed: true, items: [{ autogenerate: { directory: 'vstg' } }] },
        { label: 'MWSTG', translations: { fr: 'LTVA' }, collapsed: true, items: [{ autogenerate: { directory: 'mwstg' } }] },
        { label: 'StG', translations: { fr: 'LT' }, collapsed: true, items: [{ autogenerate: { directory: 'stg' } }] },
        { label: 'Über den ILE-HSG Steuerrechtskommentar', translations: { fr: 'À propos du Commentaire' }, slug: 'ueber' },
      ],
    }),
  ],
});
