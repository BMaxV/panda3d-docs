# -*- coding: utf-8 -*-
#
# Panda3D documentation build configuration file, created by
# sphinx-quickstart on Thu Oct  1 01:31:55 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import types
import re
from sphinx_interrogatedb import idb
from sphinx.ext import autodoc
from docutils import nodes
from panda3d.interrogatedb import *

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_autopackagesummary',
    'variations',
    'sphinx.ext.graphviz',
    'sphinxcontrib.napoleon',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.viewcode',
    'sphinx_interrogatedb',
    'sphinx.ext.intersphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Panda3D'
copyright = u'2019 Carnegie Mellon University'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.10'

# The full X.Y.Z version.
release = '1.10.8'

# Whether to generate Python or C++ documentation.  TODO:
tags.add('python')

variations = [('python', 'Python'),
              ('cpp', 'C++')]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# Set default settings for embedded graphviz diagrams.
graphviz_dot_args = [
    "-Gfontname='Lato','proxima-nova','Helvetica Neue',Arial,sans-serif",
    "-Nfontname='Lato','proxima-nova','Helvetica Neue',Arial,sans-serif",
    "-Efontname='Lato','proxima-nova','Helvetica Neue',Arial,sans-serif",
    "-Gfontsize=12.00",
    "-Nfontsize=12.00",
    "-Efontsize=12.00",
    "-Gfontcolor=#404040",
    "-Nfontcolor=#404040",
    "-Efontcolor=#404040",
    "-Gcolor=#404040",
    "-Ncolor=#404040",
    "-Ecolor=#404040",
]
graphviz_output_format = "svg"


# -- Options for HTML output ----------------------------------------------

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'style_nav_header_background': '#735cdd',
    'logo_only': True,
    'collapse_navigation': False,
    'prev_next_buttons_location': 'both',
    'style_external_links': True,
    'display_version': False,
}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Panda3D Manual"
html_logo = "_static/logo.png"
html_js_files = ['versions.js', 'searchtools.js']

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    'css_files': [
        '_static/panda.css',  # override wide tables in RTD theme
    ],
    'display_github': True,
    'github_user': 'panda3d',
    'github_repo': 'panda3d-docs',
    'github_version': version,
    'conf_py_path': '/',
    'version': version,
}

# Don't copy a _sources dir -- we already have a GitHub link
html_copy_source = False

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Panda3Ddoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'Panda3D.tex', u'Panda3D Documentation',
   u'Panda3D', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'panda3d', u'Panda3D Documentation',
     [u'Panda3D'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'Panda3D', u'Panda3D Documentation',
   u'Panda3D', 'Panda3D', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

# When running the linkcheck, don't try any example.net/org/com domains.
linkcheck_ignore = [r'https?://(.+\.)?example\.(com|net|org)(/.*)?',
                    'http://server:port/path']
linkcheck_anchors = False

# Intersphinx config.
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# Set a list of modules that do bad things when imported, and should not be
# considered for API generation.
# It's fine to keep this list here; it should never grow, because we should not
# introduce new modules that don't have proper __name__ == __main__ checks or
# rely on builtins.
autosummary_mock_imports = [
    'direct.directbase.DirectStart',
    'direct.directbase.TestStart',
    'direct.directbase.ThreeUpStart',
    'direct.directdevices.DirectFastrak',
    'direct.directdevices.DirectJoybox',
    'direct.directdevices.DirectRadamec',
    'direct.directscripts',
    'direct.directtools.DirectSession',
    'direct.directutil.DirectMySQLdb',
    'direct.directutil.DirectMySQLdbConnection',
    'direct.directutil.MemoryLeakHelpers',
    'direct.dist.pfreeze',
    'direct.filter.filterBloomI',
    'direct.filter.filterBloomX',
    'direct.filter.filterBloomY',
    'direct.filter.filterBlurX',
    'direct.filter.filterBlurY',
    'direct.filter.filterCopy',
    'direct.filter.filterDown4',
    'direct.leveleditor',
    'direct.p3d.packp3d',
    'direct.p3d.pdeploy',
    'direct.p3d.pmerge',
    'direct.p3d.ppackage',
    'direct.p3d.ppatcher',
    'direct.p3d.runp3d',
    'direct.plugin_installer.make_installer',
    'direct.plugin_installer.make_xpi',
    'direct.plugin_npapi.make_osx_bundle',
    'direct.plugin_standalone.make_osx_bundle',
    'direct.showbase.VerboseImport',
    'direct.wxwidgets.WxAppShell',
    'direct.wxwidgets.WxPandaShell',
    'direct.wxwidgets.WxPandaStart',
]

autodoc_default_options = {
    "members": None,
    "show-inheritance": None,
}
autodoc_inherit_docstrings = False
napoleon_custom_sections = ["Usage", "Features"]
autosummary_generate = True
# Prevent prepending module name to all classes/functions
add_module_names = False

# Map to camel-case for now.
autodoc_interrogatedb_mangle_type_names = False
autodoc_interrogatedb_mangle_function_names = True

# Set the directory where the .in files should be located.
try:
    import pandac
except ImportError:
    pandac = None
if pandac:
    interrogatedb_search_path = [
        os.path.join(os.path.dirname(pandac.__file__), "input")]

# Set some default graphviz attributes for the inheritance diagrams.
inheritance_graph_attrs = {
    "rankdir": "BT",
    #"splines": "ortho",
}
inheritance_node_attrs = {
    "fontsize": 11,
    "style": '""',
}
inheritance_edge_attrs = {
    "arrowsize": 0.75,
    "style": '""',
}


class ExcludeDocumenter(autodoc.Documenter):
    """Special documenter that excludes certain types from autosummary.

    It works by matching our desired excluded types, but because it has a
    special objtype not recognized by autosummary, it won't be included."""

    objtype = "exclude"

    priority = 99

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        # We only want to trigger autosummary, which always passes the empty
        # string as membername.
        if membername:
            return False

        if isinstance(member, type):
            if member.__name__.startswith("PointerToBase_ReferenceCountedVector_"):
                return True

        return False

    def generate(self, *args, **kwargs):
        # This should never even be invoked by autodoc.
        return


def resolve_reference(ref, rel, domain='py'):
    """Looks up an interrogate symbol to its canonical name.  The second
    argument is the fully qualified name it should be seen relative to, which
    may be a module name, or a module name followed by an object name.

    If found, returns a 2-tuple (type, fqname), else None."""

    # Find out which module we should be looking in.
    modname = None
    relpath = None
    rel_parts = rel.replace('::', '.').split('.')
    for i in range(len(rel_parts), 0, -1):
        try_modname = '.'.join(rel_parts[:i])
        if idb.has_module(try_modname):
            modname = try_modname
            relpath = rel_parts[i:]
            break

    if not modname:
        return None

    refpath = ref.replace('::', '.').split('.')

    # Say `rel` is "panda3d.core.NodePath.node",
    # and `ref` is "PandaNode.final", then we will try these in this order:
    # - panda3d.core::NodePath.node.PandaNode.final
    # - panda3d.core::NodePath.PandaNode.final
    # - panda3d.core::PandaNode.final

    for i in range(len(relpath), -1, -1):
        search = relpath[:i] + refpath

        if len(refpath) == 1 and i > 0 and refpath[0] == relpath[i - 1]:
            # If we are looking for a name equal to the parent scope, we are
            # probably referencing a class name from within that very class.
            # We don't want to find the constructor, so skip this.
            continue

        ifunc = idb.lookup_function(modname, search)
        if ifunc:
            if domain == 'cpp':
                func_name = interrogate_function_scoped_name(ifunc)
                return ('func', func_name)
            elif domain == 'py':
                # Grab the mangled function name.
                func_name = idb.get_function_name(ifunc, mangle=True)
                if len(search) == 1:
                    return ('func', func_name)
                else:
                    return ('meth', '.'.join(relpath[:i] + refpath[:-1] + [func_name]))

        itype = idb.lookup_type(modname, search)
        if itype:
            # Grab the original type name.
            if domain == 'cpp':
                type_name = interrogate_type_scoped_name(itype)
                if interrogate_type_is_typedef(itype):
                    return ('type', type_name)
                elif interrogate_type_is_enum(itype):
                    return ('enum', type_name)
                elif interrogate_type_is_struct(itype):
                    return ('struct', type_name)
                elif interrogate_type_is_class(itype):
                    return ('class', type_name)
                elif interrogate_type_is_union(itype):
                    return ('union', type_name)
            elif domain == 'py':
                type_name = idb.get_type_name(itype, mangle=False, scoped=True)
                return ('class', type_name)

    if len(rel_parts) >= 2 and rel_parts[0] == 'panda3d' and rel_parts[1] != 'core':
        # Look in panda3d.core instead, prefix the result with the module name.
        rel_parts[1] = 'core'
        resolved = resolve_reference(ref, '.'.join(rel_parts), domain=domain)
        if resolved and domain == 'py':
            return (resolved[0], 'panda3d.core.' + resolved[1])
        else:
            return resolved


def convert_doxygen_format(line, name, domain='py'):
    """Converts a single line of Doxygen formatting to Sphinx.
    The name argument is the fully qualified name of the current module, class
    or function, and is used to resolve references."""

    line = line.replace('<b>', '**').replace('</b>', '**')

    # Single backticks in doxygen map to doubles in Sphinx
    line = line.replace('`', '``')

    # But double backticks are literal backticks
    line = line.replace('````', '\\`')

    parent = name.rsplit('.', 1)[-1]

    # Search for method and class references.  We pick them up either when they
    # have a scoping operator, or when they end with (), or when they clearly
    # look like a class/method, or we would match all the words in the text!
    pattern = re.compile(r'([a-zA-Z_][a-zA-Z0-9_.:]*)\(\)|([a-zA-Z_][a-zA-Z0-9_]*::[a-zA-Z_][a-zA-Z0-9_.:]*)(\(\))?|([a-zA-Z_]+[A-Z0-9_][a-zA-Z0-9_.:]*)(\(\))?')
    words = line.split(' ')
    in_backticks = False
    for i, word in enumerate(words):
        if '``' in word:
            if word.count('``') % 2 == 1:
                # This opens/closes a backtick block spanning multiple words.
                in_backticks = not in_backticks
                continue

        if in_backticks:
            continue

        if word.endswith('.') or word.endswith(',') or word.endswith(';'):
            # Punctuation.
            suffix = word[-1]
            word = word[:-1]
        else:
            suffix = ''

        if word.endswith(')') and word.count(')') > word.count('('):
            # It could be the last word in a parenthesized statement.
            word = word[:-1]
            suffix = ')' + suffix

        # Don't replace the class name on the page of the class itself, unless
        # it's already in backticks.
        if word.rstrip('()') == parent:
            continue

        word = word.strip('`')

        m = re.fullmatch(pattern, word)
        if not m:
            continue

        plural = False

        result = resolve_reference(word.rstrip('()'), name, domain=domain)
        if not result and word.endswith('s') and '::' not in word and word[:-1] != parent:
            # Detect use of plural in references to classes.
            result = resolve_reference(word[:-1], name, domain=domain)
            plural = True

        if not result:
            continue

        typ, target = result

        if plural:
            words[i] = ':{0}:{1}:`{2} <{3}>`{4}'.format(domain, typ, word, target, suffix)
        elif ('.' in target or '::' in target) and '::' not in word:
            # The original wasn't scoped, so only use the last component.
            words[i] = ':{0}:{1}:`~{2}`{3}'.format(domain, typ, target, suffix)
        else:
            words[i] = ':{0}:{1}:`{2}`{3}'.format(domain, typ, target, suffix)

        #print("replaced", word, "with", words[i])

    return ' '.join(words)


def convert_doxygen_docstring(lines, name, domain='py'):
    """Converts a doxygen-style C++ block comment to a Sphinx-style one.
    The name argument is the fully qualified name of the current module, class
    or function, and is used to resolve references."""

    lines = lines[:]
    newlines = []
    indent = 0
    reading_desc = False

    while lines:
        line = lines.pop(0)
        if line.startswith("////"):
            continue

        line = line.rstrip()
        if line.startswith('///<'):
            strline = line[4:]
        else:
            strline = line

        strline = strline.lstrip('/ \t')

        if strline == "**" or strline == "*/":
            continue

        if strline.startswith("** "):
            strline = strline[3:]
        elif strline.startswith("* "):
            strline = strline[2:]
        elif strline == "*":
            strline = ""

        strline = strline.lstrip(' \t')

        if strline.startswith('@'):
            special = strline.split(' ', 1)[0][1:]
            if special == 'par' and strline.endswith(':') and lines and '@code' in lines[0]:
                newlines.append('   '*indent + strline[5:] + ':')
                newlines.append('')
                line = lines.pop(0)
                offset = line.index('@code')
                while lines:
                    line = lines.pop(0)
                    if '@endverbatim' in line or '@endcode' in line:
                        break
                    newlines.append('   ' + line[offset:])

                newlines.append('')
                continue
            elif special == "verbatim" or special == "code":
                if newlines and newlines[-1]:
                    newlines.append('')

                newlines.append('.. code-block:: guess')
                newlines.append('')
                offset = line.index('@' + special)
                while lines:
                    line = lines.pop(0)
                    if '@endverbatim' in line or '@endcode' in line:
                        break
                    newlines.append('   ' + line[offset:])

                newlines.append('')
                continue
            elif special == "f[":
                if newlines and newlines[-1]:
                    newlines.append('')

                newlines.append('.. math::')
                newlines.append('')
                offset = line.index('@' + special)
                while lines:
                    line = lines.pop(0)
                    if '@f]' in line:
                        break
                    newlines.append('   ' + line[offset:])

                newlines.append('')
                continue
            elif special == 'param':
                #TODO
                #if extra is not None:
                #    _, name, desc = strline.split(' ', 2)
                #    extra['param:' + name] = desc
                continue
            elif special == 'deprecated':
                if newlines and newlines[-1]:
                    newlines.append('')

                _, value = strline.split(' ', 1)

                # I'd love to use the proper Sphinx deprecated tag, but it
                # requires a version number, whereas Doxygen doesn't.
                newlines.append('*Deprecated:* ' + convert_doxygen_format(value, name, domain))
                newlines.append('')
                continue
            elif special in ('brief', 'return', 'returns'):
                #TODO
                #if extra is not None:
                #    _, value = strline.split(' ', 1)
                #    extra[special] = value
                continue
            elif special == 'details':
                strline = strline[9:]
            elif special == 'sa' or special == 'see':
                if newlines and newlines[-1]:
                    newlines.append('')

                _, value = strline.split(' ', 1)
                values = value.split(',')

                for i, value in enumerate(values):
                    result = resolve_reference(value.partition('(')[0], name, domain=domain)
                    if result:
                        values[i] = ':{0}:{1}:`{2}`'.format(domain, *result)
                    else:
                        values[i] = ':{0}:obj:`{1}`'.format(domain, value)

                if special == 'see':
                    newlines.append('See {}.'.format(', '.join(values)))
                else:
                    newlines.append('See also {}.'.format(', '.join(values)))
                newlines.append('')
                continue
            elif special in ('note', 'warning'):
                if newlines and newlines[-1]:
                    newlines.append('')

                newlines.append('.. %s:: ' % (special))
                newlines.append('')
                newlines.append('   ' + convert_doxygen_format(strline[2 + len(special):], name, domain))
                while lines and lines[0].strip(' *\t/'):
                    line = lines.pop(0).lstrip(' *\t')
                    newlines.append('   ' + convert_doxygen_format(line, name, domain))

                newlines.append('')
                continue
            elif special == 'since':
                if newlines and newlines[-1]:
                    newlines.append('')

                newlines.append('.. versionadded:: ' + strline[7:])
                newlines.append('')
                continue
            else:
                print("Unhandled documentation tag: @" + special)

        if strline or len(newlines) > 0:
            newlines.append('   '*indent + convert_doxygen_format(strline, name, domain))

    return newlines


def on_autodoc_skip_member(app, what, name, obj, skip, options):
    # Always document constructors.
    if name == '__init__':
        return False

    # Don't document method aliases.  This also has the side-effect of
    # excluding private members, which is OK.
    if isinstance(obj, types.FunctionType) and obj.__name__ != name:
        return True


def on_autodoc_process_docstring(app, what, name, obj, options, lines):
    # This is a temporary hack for a particularly nasty docstring in
    # direct.fsm.FourState and direct.fsm.FourStateAI that was badly
    # formatted.  It can be removed once a new version of Panda3D is
    # released with the offending docstring fixed.

    if (name == 'direct.fsm.FourState.FourState.__init__' or
        name == 'direct.fsm.FourStateAI.FourStateAI.__init__') \
       and 'are used:' in lines:
        lines[lines.index('are used:')] = 'are used::'

    if lines:
        line0 = lines[0].lstrip()
        if line0.startswith('/**') or line0.startswith('// '):
            domain = app.env.temp_data.get('default_domain')
            domain = domain.name if domain else 'py'
            lines[:] = convert_doxygen_docstring(lines, name, domain)


def on_missing_reference(app, env, node, contnode):
    # Resolver for interrogate classes that supports either snake case or camel
    # case naming.  Depending on the variation that is active, it will link to
    # either the Python or C++ reference as appropriate.

    target = node['reftarget']

    # Figure out which part is the module and which part is the class.
    prefix = ''
    module = 'panda3d.core'
    if target.startswith('panda3d.'):
        parts = target.split('.', 2)
        if len(parts) == 2:
            # It's trying to resolve a reference to a module; we can't help
            # with that.
            return

        module = '.'.join(parts[:2])
        prefix = module + '.'
        target = '.'.join(parts[2:])
    else:
        # Something like .core.NodePath, perhaps?
        modpart = target.split('.', 1)[0]
        if idb.has_module('panda3d.' + modpart):
            module = 'panda3d.' + modpart
            prefix = modpart + '.'
            target = target.split('.', 1)[1]

    variation = getattr(env.app.builder, 'current_variation', None)
    if variation and variation[0] == 'cpp':
        domain = env.domains['cpp']
    else:
        domain = env.domains['py']

    resolved = target and resolve_reference(target, module, domain=domain.name)

    typ = node['reftype']
    if domain.name == 'cpp' and typ == 'meth':
        # C++ domain doesn't have "meth", everything is "func" there.
        typ = 'func'

    if resolved and (resolved[0] == typ or typ == 'obj'):
        refdoc = node.get('refdoc', env.docname)

        # Try to match the original, but with the canonical mangling
        # (depending on Python versus C++)
        if len(contnode.children) and not node.get('refexplicit'):
            oldtext = contnode.children[0].astext()

            if domain.name == 'cpp':
                text = resolved[1]
                text = '::'.join(text.split('::')[-oldtext.replace('.', '::').count('.')-1:])
            else:
                text = prefix + resolved[1]
                text = '.'.join(text.split('.')[-oldtext.count('.')-1:])

            if oldtext.endswith("()"):
                text += "()"

            contnode.children[0] = nodes.Text(text)

        elif domain.name == 'cpp':
            # Work around a bug in the C++ resolver, which expects this
            # text node to be the child of an Element.  I picked a
            # decoration element since it happens not to translate to
            # anything (not sure what its purpose is).
            if isinstance(contnode, nodes.Text):
                contnode = nodes.decoration('', contnode)

        elif domain.name == 'py' and len(contnode.children) and node.get('refexplicit'):
            # Custom text was used.  Replace snake_case with camelCase in it.
            # This allows doing something like:
            # :meth:`model.set_color() <.NodePath.set_color>`
            # ..and still have it translate to the correct casing.
            oldpart = target.rsplit('.', 1)[-1]
            newpart = resolved[1].rsplit('.', 1)[-1]
            if oldpart != newpart:
                text = contnode.children[0].astext()
                text = text.replace('::', '.')
                text = text.replace('.' + oldpart + '(', '.' + newpart + '(')
                if text.startswith(oldpart + '('):
                    text = newpart + text[len(oldpart):]
                contnode.children[0] = nodes.Text(text)

        # C++ references don't have a module prefix and use :: for scoping
        if domain.name == 'cpp':
            target = resolved[1]
            if typ == 'obj':
                # Another bug workaround
                typ = resolved[0]
            if typ in ('enum', 'class', 'struct', 'union') and resolved[0] == 'type':
                # Squelch warning
                typ = resolved[0]
        else:
            target = prefix + resolved[1]

        return domain.resolve_xref(env, refdoc, app.builder, typ, target, node, contnode)


def on_builder_inited(app):
    app.builder.get_relative_uri = \
        lambda from_, to, typ=None: \
            app.config.html_absolute_url_root + app.config.version + '/' + app.builder.get_target_uri(to, typ)


def on_html_page_context(app, pagename, templatename, context, doctree):
    def pathto(otheruri, resource=False, baseuri=None):
        if resource and '://' in otheruri:
            # allow non-local resources given by scheme
            return otheruri

        if not resource:
            otheruri = app.builder.get_target_uri(otheruri)

        if baseuri is None:
            baseuri = app.config.html_absolute_url_root + version + '/'

        if not baseuri.startswith('/'):
            raise BaseURIError('"baseuri" must be absolute')

        if not otheruri.startswith('/'):
            otheruri = '/' + otheruri

        if otheruri:
            if baseuri.endswith('/'):
                baseuri = baseuri[:-1]
            otheruri = baseuri + otheruri

        uri = otheruri or '#'
        return uri

    context['pathto'] = pathto


def on_config_inited(app, config):
    if config.html_absolute_url_root:
        app.connect('builder-inited', on_builder_inited)
        app.connect('html-page-context', on_html_page_context)

        # This normally runs before our hook, so it still picks up the old
        # pathto, hence we need to register it again
        from sphinx.builders.html import setup_js_tag_helper
        app.connect('html-page-context', setup_js_tag_helper)

    # Used in searchbox.html.
    if config.html_link_suffix is not None:
        config.html_context['link_suffix'] = config.html_link_suffix
    elif config.html_file_suffix is not None:
        config.html_context['link_suffix'] = config.html_file_suffix
    else:
        config.html_context['link_suffix'] = '.html'


# This is an awful hack to get the inheritance graphs to incorporate the
# current variation into the links properly, and, at the same time, not
# generate the arrow connections inverted. :-/
def generate_dot(self, name, urls={}, env=None,
                 graph_attrs={}, node_attrs={}, edge_attrs={}):
    g_attrs = self.default_graph_attrs.copy()
    n_attrs = self.default_node_attrs.copy()
    e_attrs = self.default_edge_attrs.copy()
    g_attrs.update(graph_attrs)
    n_attrs.update(node_attrs)
    e_attrs.update(edge_attrs)
    if env:
        g_attrs.update(env.config.inheritance_graph_attrs)
        n_attrs.update(env.config.inheritance_node_attrs)
        e_attrs.update(env.config.inheritance_edge_attrs)

    res = []  # type: List[str]
    res.append('strict digraph %s {\n' % name)
    res.append(self._format_graph_attrs(g_attrs))

    for name, fullname, bases, tooltip in sorted(self.class_info):
        if name == 'DTOOL_SUPER_BASE':
            continue

        # Write the node
        this_node_attrs = n_attrs.copy()
        if fullname in urls:
            url = urls[fullname]
            # Fix the URL reference to contain the current variation.
            # Also strip off the # reference at the end, since our classes
            # are defined near the top of each file anyway.
            if env and env.config.graphviz_output_format.lower() == 'svg' and \
               getattr(env.app.builder, 'current_variation', None):
                url = '../' \
                    + env.app.builder.current_variation[0] \
                    + '/reference/' \
                    + os.path.basename(url).split('#', 1)[0]

            this_node_attrs['URL'] = '"%s"' % url
            this_node_attrs['target'] = '"_top"'
        if tooltip:
            this_node_attrs['tooltip'] = tooltip
        res.append('  "%s" [%s];\n' %
                   (name, self._format_node_attrs(this_node_attrs)))

        # Write the edges
        for base_name in bases:
            if base_name == 'DTOOL_SUPER_BASE':
                continue
            res.append('  "%s" -> "%s" [%s];\n' %
                       (name, base_name,
                        self._format_node_attrs(e_attrs)))
    res.append('}\n')
    return ''.join(res)


def setup(app):
    from sphinx.ext.inheritance_diagram import InheritanceGraph
    InheritanceGraph.generate_dot = generate_dot

    app.add_config_value('html_absolute_url_root', None, 'html')
    app.connect('config-inited', on_config_inited)

    app.connect('autodoc-skip-member', on_autodoc_skip_member)
    app.connect('autodoc-process-docstring', on_autodoc_process_docstring)

    app.connect('missing-reference', on_missing_reference, priority=901)

    app.add_autodocumenter(ExcludeDocumenter)
