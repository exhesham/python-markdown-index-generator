* **[Goal](#goal)**
* **[Syntax](#syntax)**
* **[Operate](#operate)**

# Goal

Table of contents in mark down files is syntax-complicated. This code will auto-generate it for you. so all left to do is copy-paste.

# Syntax
Say you have a markdown readme file as follows:

```
//## Post Publish
bla bla bla...
```
The script will generate the next ToC:
`* **[Post-Publish](#post-publish)**`

For this page, the output would be:
```
   * **[Goal](#goal)**
   * **[Syntax](#syntax)**
   * **[Operate](#operate)**
```

# Operate

Edit the md file for your need and run it as is.

```
python -m markdown_toc --file [your file path]
```
