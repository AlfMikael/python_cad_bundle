r"""
Currently, this package is experimental and may change in the future.
"""
from __future__ import absolute_import



# start delvewheel patch
def _delvewheel_patch_1_4_0():
    import ctypes
    import os
    import platform
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, '.'))
    is_conda_cpython = platform.python_implementation() == 'CPython' and (hasattr(ctypes.pythonapi, 'Anaconda_GetVersion') or 'packaged by conda-forge' in sys.version)
    if sys.version_info[:2] >= (3, 8) and not is_conda_cpython or sys.version_info[:2] >= (3, 10):
        if os.path.isdir(libs_dir):
            os.add_dll_directory(libs_dir)
    else:
        load_order_filepath = os.path.join(libs_dir, '.load-order-cadquery_ocp-7.7.1')
        if os.path.isfile(load_order_filepath):
            with open(os.path.join(libs_dir, '.load-order-cadquery_ocp-7.7.1')) as file:
                load_order = file.read().split()
            for lib in load_order:
                lib_path = os.path.join(os.path.join(libs_dir, lib))
                if os.path.isfile(lib_path) and not ctypes.windll.kernel32.LoadLibraryExW(ctypes.c_wchar_p(lib_path), None, 0x00000008):
                    raise OSError('Error loading {}; {}'.format(lib, ctypes.FormatError()))


_delvewheel_patch_1_4_0()
del _delvewheel_patch_1_4_0
# end delvewheel patch

import sys


def _windows_dll_path():
    import os
    _vtk_python_path = 'Lib/site-packages/vtkmodules'
    _vtk_dll_path = 'Library/bin'
    # Compute the DLL path based on the location of the file and traversing up
    # the installation prefix to append the DLL path.
    _vtk_dll_directory = os.path.dirname(os.path.abspath(__file__))
    # Loop while we have components to remove.
    while _vtk_python_path not in ('', '.', '/'):
        # Strip a directory away.
        _vtk_python_path = os.path.dirname(_vtk_python_path)
        _vtk_dll_directory = os.path.dirname(_vtk_dll_directory)
    _vtk_dll_directory = os.path.join(_vtk_dll_directory, _vtk_dll_path)
    if os.path.exists(_vtk_dll_directory):
        # We never remove this path; it is required for VTK to work and there's
        # no scope where we can easily remove the directory again.
        _ = os.add_dll_directory(_vtk_dll_directory)

    # Build tree support.
    try:
        from . import _build_paths

        # Add any paths needed for the build tree.
        for path in _build_paths.paths:
            if os.path.exists(path):
                _ = os.add_dll_directory(path)
    except ImportError:
        # Relocatable install tree (or non-Windows).
        pass


# CPython 3.8 added behaviors which modified the DLL search path on Windows to
# only search "blessed" paths. When importing SMTK, ensure that SMTK's DLLs are
# in this set of "blessed" paths.
if sys.version_info >= (3, 8) and sys.platform == 'win32':
    _windows_dll_path()


#------------------------------------------------------------------------------
# this little trick is for static builds of VTK. In such builds, if
# the user imports this Python package in a non-statically linked Python
# interpreter i.e. not of the of the VTK-python executables, then we import the
# static components importer module.
def _load_vtkmodules_static():
    if 'vtkmodules_vtkCommonCore' not in sys.builtin_module_names:
        import _vtkmodules_static

#_load_vtkmodules_static()


#------------------------------------------------------------------------------
# list the contents
__all__ = [
    'vtkCommonCore',
    'vtkWebCore',
    'vtkCommonMath',
    'vtkCommonTransforms',
    'vtkCommonDataModel',
    'vtkCommonExecutionModel',
    'vtkIOCore',
    'vtkImagingCore',
    'vtkIOImage',
    'vtkIOXMLParser',
    'vtkIOXML',
    'vtkCommonMisc',
    'vtkFiltersCore',
    'vtkRenderingCore',
    'vtkRenderingContext2D',
    'vtkRenderingFreeType',
    'vtkRenderingSceneGraph',
    'vtkRenderingVtkJS',
    'vtkIOExport',
    'vtkWebGLExporter',
    'vtkInteractionStyle',
    'vtkFiltersGeneral',
    'vtkFiltersSources',
    'vtkInteractionWidgets',
    'vtkViewsCore',
    'vtkViewsInfovis',
    'vtkCommonColor',
    'vtkViewsContext2D',
    'vtkTestingRendering',
    'vtkPythonContext2D',
    'vtkImagingMath',
    'vtkRenderingHyperTreeGrid',
    'vtkRenderingUI',
    'vtkRenderingOpenGL2',
    'vtkRenderingVolume',
    'vtkRenderingVolumeOpenGL2',
    'vtkRenderingLabel',
    'vtkRenderingLOD',
    'vtkRenderingLICOpenGL2',
    'vtkRenderingImage',
    'vtkRenderingContextOpenGL2',
    'vtkIOVeraOut',
    'vtkIOTecplotTable',
    'vtkIOSegY',
    'vtkIOParallelXML',
    'vtkIOLegacy',
    'vtkIOGeometry',
    'vtkIOParallel',
    'vtkIOPLY',
    'vtkIOMovie',
    'vtkIOOggTheora',
    'vtkIONetCDF',
    'vtkIOMotionFX',
    'vtkIOMINC',
    'vtkIOLSDyna',
    'vtkIOInfovis',
    'vtkIOImport',
    'vtkParallelCore',
    'vtkIOIOSS',
    'vtkIOVideo',
    'vtkIOExportPDF',
    'vtkRenderingGL2PSOpenGL2',
    'vtkIOExportGL2PS',
    'vtkIOExodus',
    'vtkIOEnSight',
    'vtkIOCityGML',
    'vtkIOChemistry',
    'vtkIOCesium3DTiles',
    'vtkIOCONVERGECFD',
    'vtkIOHDF',
    'vtkIOCGNSReader',
    'vtkIOAsynchronous',
    'vtkIOAMR',
    'vtkInteractionImage',
    'vtkImagingStencil',
    'vtkImagingStatistics',
    'vtkImagingGeneral',
    'vtkImagingMorphological',
    'vtkImagingFourier',
    'vtkIOSQL',
    'vtkImagingSources',
    'vtkInfovisCore',
    'vtkGeovisCore',
    'vtkInfovisLayout',
    'vtkRenderingAnnotation',
    'vtkImagingHybrid',
    'vtkImagingColor',
    'vtkFiltersTopology',
    'vtkFiltersSelection',
    'vtkFiltersSMP',
    'vtkFiltersPython',
    'vtkFiltersProgrammable',
    'vtkFiltersModeling',
    'vtkFiltersPoints',
    'vtkFiltersVerdict',
    'vtkFiltersStatistics',
    'vtkFiltersImaging',
    'vtkFiltersExtraction',
    'vtkFiltersGeometry',
    'vtkFiltersHybrid',
    'vtkFiltersTexture',
    'vtkFiltersParallel',
    'vtkFiltersParallelImaging',
    'vtkFiltersGeneric',
    'vtkCommonComputationalGeometry',
    'vtkFiltersFlowPaths',
    'vtkFiltersAMR',
    'vtkDomainsChemistry',
    'vtkDomainsChemistryOpenGL2',
    'vtkFiltersHyperTree',
    'vtkCommonPython',
    'vtkChartsCore',
    'vtkCommonSystem',
    'gtk',
    'numpy_interface',
    'qt',
    'test',
    'tk',
    'util',
    'wx',
]

#------------------------------------------------------------------------------
# get the version
__version__ = "9.2.5"
